class Solution:

    def superEggDrop(self, K, N):
        dp = dict()

        def recursive(k, n):
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in dp:
                return dp[k, n]
            res = float('INF')
            l = 1
            r = n + 1
            while l <= r:
                m = int((l + r) / 2)
                v1 = recursive(k, n - m)
                v2 = recursive(k - 1, m - 1)
                res = min(res, max(v1, v2) + 1)
                if v1 < v2:
                    r = m - 1
                elif v1 > v2:
                    l = m + 1
                else:
                    break
            dp[k, n] = res
            return res
        import sys
        sys.setrecursionlimit(3000)
        res = recursive(K, N)
        return res
