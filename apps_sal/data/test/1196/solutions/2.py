def compress(bstr):
    pk, pc = None, None

    for block in bstr:
        if pc is None:
            pk, pc = block
        elif pc == block[1]:
            pk += block[0]
        else:
            yield  pk, pc
            pk, pc = block

    if pc is not None:
        yield pk, pc


def find1(text, query):
    (bk, bc), = query
    return sum(k-bk+1 for k, c in text if c == bc and k >= bk)


class Query:
    def __init__(self, query):
        self._query = query
        self._len = len(query)
        self._suffixes = {}

    def precompute(self):
        for i in range(self._len-1):
            self._suffix(i)

    def _suffix(self, i, pblock=None):
        if not i:
            return None

        if pblock is None and i is not None:
            pblock = self._query[i]

        if (i, pblock) in self._suffixes:
            return self._suffixes[i, pblock]
        else:
            sfx = self.next(self._suffix(i-1), pblock)
            self._suffixes[i, pblock] = sfx
            return sfx

    def _match(self, i, block):
        if i == 0 or i == self._len -1:
            return (block[1] == self._query[i][1]
                    and block[0] >= self._query[i][0])
        else:
            return block == self._query[i]

    def next(self, i, block, pblock=None):
        while True:
            if i is None:
                return 0 if self._match(0, block) else None
            elif i < self._len-1:
                if self._match(i+1, block):
                    return i+1
                else:
                    i = self._suffix(i)
            else:
                i = self._suffix(i, pblock)
                pblock = None

    def is_match(self, i):
        return i == self._len-1


def find2(text, query):
    qobj = Query(query)
    qobj.precompute()
    i = None
    pblock = None
    c = 0
    for block in text:
        i, pblock = qobj.next(i, block, pblock), block
        if qobj.is_match(i):
            c += 1
    return c


def find(text, query):
    text = list(compress(text))
    query = list(compress(query))
    return (find1 if len(query) == 1 else find2)(text, query)


def parse_block(s):
    k, c = s.split('-')
    return int(k), c


def get_input():
    n, m = list(map(int, input().split()))
    text = list(map(parse_block, input().split()))
    assert len(text) == n
    query = list(map(parse_block, input().split()))
    assert len(query) == m
    return text, query


def __starting_point():
    print(find(*get_input()))

__starting_point()
