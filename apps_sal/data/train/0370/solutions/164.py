class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        N = len(A)
        p = [i for i in range(N)]

        def uf(i):
            if i == p[i]:
                return i
            p[i] = uf(p[i])
            return p[i]
        dt = collections.defaultdict(set)

        def prime_factor(index):
            i = A[index]
            while i % 2 == 0:
                dt[2].add(index)
                i //= 2
            for j in range(3, int(A[index] ** 0.5) + 1, 2):
                while i % j == 0:
                    dt[j].add(index)
                    i //= j
            if i > 2:
                dt[i].add(index)
        cnt = collections.defaultdict(int)
        for i in range(N):
            prime_factor(i)
        for (_, v) in list(dt.items()):
            pi = uf(v.pop())
            while v:
                pj = uf(v.pop())
                p[pj] = pi
        res = 1
        for i in range(N):
            pi = uf(i)
            cnt[pi] += 1
            res = max(res, cnt[pi])
        return res
