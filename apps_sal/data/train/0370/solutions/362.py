class DisjointSets:

    def __init__(self, n: int):
        self.p = n * [-1]
        self.s = n * [1]

    def find(self, i: int) -> int:
        r = i
        while self.p[r] != -1:
            r = self.p[r]
        while i != r:
            (self.p[i], i) = (r, self.p[i])
        return r

    def merge(self, i: int, j: int) -> int:
        i = self.find(i)
        j = self.find(j)
        if i != j:
            if self.s[i] < self.s[j]:
                (i, j) = (j, i)
            self.p[j] = i
            self.s[i] += self.s[j]
        return i


class Solution:

    def largestComponentSize(self, a: List[int]) -> int:
        (n, m) = (len(a), max(a))
        acnt = (m + 1) * [0]
        for ai in a:
            acnt[ai] += 1
        acnt = list(accumulate(acnt))
        ainv = n * [0]
        for i in range(n - 1, -1, -1):
            acnt[a[i]] -= 1
            ainv[acnt[a[i]]] = i
        acnt = acnt[1:] + [n]
        djs = DisjointSets(n)
        isp = (m + 1) * [True]
        for i in range(2, m + 1):
            if not isp[i]:
                continue
            p = -1
            for j in range(i, m + 1, i):
                isp[j] = False
                for k in ainv[acnt[j - 1]:acnt[j]]:
                    if p >= 0:
                        djs.merge(p, k)
                    p = k
        return max(djs.s)
