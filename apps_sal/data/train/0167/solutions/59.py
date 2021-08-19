class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}

        def dp(k, n):
            if k <= 0:
                return 0
            if k == 1:
                return n
            if n <= 1:
                return n
            if (k, n) in memo:
                return memo[k, n]
            (l, r) = (1, n + 1)
            while l < r:
                mid = l + (r - l) // 2
                broken = dp(k - 1, mid - 1)
                unbroken = dp(k, n - mid)
                if broken >= unbroken:
                    r = mid
                else:
                    l = mid + 1
            memo[k, n] = 1 + dp(k - 1, l - 1)
            return memo[k, n]
        return dp(K, N)
