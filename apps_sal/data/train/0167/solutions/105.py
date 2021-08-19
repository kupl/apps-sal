class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()
        return self.dp(K, N, memo)

    def dp(self, k, n, memo):
        if k == 1:
            return n
        if n == 0:
            return 0
        if (k, n) in memo:
            return memo[k, n]
        res = float('inf')
        '\n        for i in range(1, n+1):\n            res = min(res,  max(self.dp(k-1, i-1, memo), self.dp(k, n-i, memo)) + 1 )\n        '
        (lo, hi) = (1, n)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            broken = self.dp(k - 1, mid - 1, memo)
            not_broken = self.dp(k, n - mid, memo)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)
        memo[k, n] = res
        return res
