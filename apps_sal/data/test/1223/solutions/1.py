import bisect


class SqrtSet:
    def __init__(self, block_limit=201):
        self.key = []
        self.child = [[]]
        self.block_limit = block_limit

    def search_lower(self, key):
        if key is None:
            return None
        ret = None
        i = bisect.bisect_left(self.key, key)
        if i != 0:
            ret = self.key[i - 1]
        block = self.child[i]
        i = bisect.bisect_left(block, key)
        if i != 0:
            ret = block[i - 1]
        return ret

    def search_higher(self, key):
        if key is None:
            return None
        ret = None
        i = bisect.bisect_right(self.key, key)
        if i != len(self.key):
            ret = self.key[i]
        block = self.child[i]
        i = bisect.bisect_right(block, key)
        if i != len(block):
            ret = block[i]
        return ret

    def insert(self, key):
        i = bisect.bisect(self.key, key)
        block = self.child[i]
        bisect.insort(block, key)
        if len(block) == self.block_limit:
            sep = self.block_limit // 2
            self.key.insert(i, block[sep])
            self.child.insert(i + 1, block[sep + 1:])
            self.child[i] = block[:sep]

    def dump(self):
        for b in self.child:
            print(len(b), end=" ")
        print("")


def main():
    n = int(input())
    p = list(map(int, input().split()))
    idx = [0] * n
    for i in range(0, n):
        idx[i] = i
    idx.sort(key=lambda i: - p[i])
    t = SqrtSet()
    t.insert(-1)
    t.insert(n)
    ans = 0
    for i in idx:
        nex = t.search_higher(i)
        nexnex = t.search_higher(nex)
        pre = t.search_lower(i)
        prepre = t.search_lower(pre)
        if prepre != None:
            ans += p[i] * (pre - prepre) * (nex - i)
        if nexnex != None:
            ans += p[i] * (i - pre) * (nexnex - nex)
        t.insert(i)
    print(ans)


main()
