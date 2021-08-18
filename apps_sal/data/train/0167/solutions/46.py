class Solution:
    def superEggDrop1(self, K: int, N: int) -> int:
        memo = [[2**31 - 1] * (N + 1) for _ in range(K + 1)]

        def dp(k, n):
            if k == 0:
                return 0
            if k == 1:
                return n
            if n <= 1:
                return n

            if memo[k][n] < 2**31 - 1:
                return memo[k][n]

            ans = memo[k][n]
            for i in range(1, n + 1):
                ans = min(ans, 1 + max(dp(k - 1, i - 1), dp(k, n - i)))
            memo[k][n] = ans
            return ans
        return dp(K, N)

    def superEggDrop(self, K: int, N: int) -> int:
        memo = [[2**31 - 1] * (N + 1) for _ in range(K + 1)]

        def dp(k, n):
            if k == 0:
                return 0
            if k == 1:
                return n
            if n <= 1:
                return n

            if memo[k][n] < 2**31 - 1:
                return memo[k][n]

            left = 1
            right = n + 1
            while left < right:
                mid = left + (right - left) // 2
                if dp(k - 1, mid - 1) >= dp(k, n - mid):
                    right = mid
                else:
                    left = mid + 1

            memo[k][n] = 1 + max(dp(k - 1, left - 1), dp(k, n - left))
            return memo[k][n]
        return dp(K, N)
