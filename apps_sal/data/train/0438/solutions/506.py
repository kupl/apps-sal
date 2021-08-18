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
        for i, b in enumerate(arr):
            b -= 1
            fliped[b] = True
            bl = 1
            if b > 0 and fliped[b - 1]:
                s = dsu.find(b - 1)
                sa = area[s]
                cnt[sa] -= 1
                dsu.union(s, b)
                bl += sa
            if b < len(arr) - 1 and fliped[b + 1]:
                s = dsu.find(b + 1)
                sa = area[s]
                cnt[sa] -= 1
                dsu.union(s, b)
                bl += sa
            s = dsu.find(b)
            area[s] = bl
            cnt[bl] += 1
            if cnt[m] > 0:
                res.append(i)
        return res[-1] + 1 if res else -1
