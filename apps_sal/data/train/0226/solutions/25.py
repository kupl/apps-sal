class Solution:

    def numSquarefulPerms(self, A: List[int]) -> int:
        d = defaultdict(int)
        res = 0
        ps = {}
        i = 0
        while i * i <= 2 * max(A):
            ps[i * i] = True
            i += 1

        def ok(x):
            return x in ps

        def solve(x):
            nonlocal res
            if not len(d):
                res += 1
                return
            for k in list(d.keys()):
                if not ok(x + k):
                    continue
                d[k] -= 1
                if d[k] == 0:
                    del d[k]
                solve(k)
                d[k] += 1
        for x in A:
            d[x] += 1
        for k in list(d.keys()):
            d[k] -= 1
            if not d[k]:
                del d[k]
            solve(k)
            d[k] += 1
        return res
