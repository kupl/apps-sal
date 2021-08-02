from bisect import*


class SqrtSet:
    def __init__(self, block_limit=201):
        self.key = []
        self.child = [[]]
        self.block_limit = block_limit

    def le(self, key):
        ret = key
        i = bisect_left(self.key, key)
        if i:
            ret = self.key[i - 1]
        block = self.child[i]
        i = bisect_left(block, key)
        if i:
            ret = block[i - 1]
        return ret

    def ge(self, key):
        ret = key
        i = bisect(self.key, key)
        if i < len(self.key):
            ret = self.key[i]
        block = self.child[i]
        i = bisect(block, key)
        if i < len(block):
            ret = block[i]
        return ret

    def insert(self, key):
        i = bisect(self.key, key)
        block = self.child[i]
        insort(block, key)
        if len(block) == self.block_limit:
            sep = self.block_limit // 2
            self.key.insert(i, block[sep])
            self.child.insert(i + 1, block[sep + 1:])
            self.child[i] = block[:sep]


def main():
    n, *p = map(int, open(0).read().split())
    l = [0] * n
    for i, v in enumerate(p, 1):
        l[v - 1] = i
    t = SqrtSet()
    insert, le, ge = t.insert, t.le, t.ge
    insert(0), insert(n + 1)
    a = 0
    for i, v in list(enumerate(l, 1))[::-1]:
        f, b = ge(v), le(v)
        g, c = ge(f), le(b)
        a += i * ((f - v) * (b - c) + (v - b) * (g - f))
        insert(v)
    print(a)


main()
