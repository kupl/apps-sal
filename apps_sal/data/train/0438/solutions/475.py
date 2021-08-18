from collections import Counter


class DSU:
    def __init__(self, n):
        self.dic = [i for i in range(n)]

    def find(self, n1):
        if self.dic[n1] != n1:
            self.dic[n1] = self.find(self.dic[n1])
        return self.dic[n1]

    def union(self, n1, n2):
        s1 = self.find(n1)
        s2 = self.find(n2)
        self.dic[s2] = s1


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        cnt = Counter()
        area = Counter()
        fliped = [False for _ in arr]
        dsu = DSU(len(arr))
        res = []

        def union_bits(b, bi):
            if not (0 <= bi < len(arr) and fliped[bi]):
                return 0
            s = dsu.find(bi)
            sa = area[s]
            cnt[sa] -= 1
            dsu.union(s, b)
            return sa
        for i, b in enumerate(arr):
            b -= 1
            fliped[b] = True
            ba = 1
            ba += union_bits(b, b - 1)
            ba += union_bits(b, b + 1)
            s = dsu.find(b)
            area[s] = ba
            cnt[ba] += 1
            if cnt[m] > 0:
                res.append(i)
        return res[-1] + 1 if res else -1
