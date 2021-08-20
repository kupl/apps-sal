class Solution:

    def superEggDrop1(self, K: int, N: int) -> int:
        memo = [[2 ** 31 - 1] * (N + 1) for _ in range(K + 1)]

        def dp(k, n):
            if k == 0:
                return 0
            if k == 1:
                return n
            if n <= 1:
                return n
            if memo[k][n] < 2 ** 31 - 1:
                return memo[k][n]
            ans = memo[k][n]
            for i in range(1, n + 1):
                ans = min(ans, 1 + max(dp(k - 1, i - 1), dp(k, n - i)))
            memo[k][n] = ans
            return ans
        return dp(K, N)

    def superEggDrop3(self, K: int, N: int) -> int:
        memo = [[2 ** 31 - 1] * (N + 1) for _ in range(K + 1)]

        def dp(k, n):
            if k == 0:
                return 0
            if k == 1:
                return n
            if n <= 1:
                return n
            if memo[k][n] < 2 ** 31 - 1:
                return memo[k][n]
            left = 1
            right = n + 1
            res = 2 ** 31 - 1
            while left < right:
                mid = left + (right - left) // 2
                broken = dp(k - 1, mid - 1)
                notbroken = dp(k, n - mid)
                if broken >= notbroken:
                    right = mid
                    res = min(res, broken + 1)
                else:
                    left = mid + 1
                    res = min(res, notbroken + 1)
            memo[k][n] = res
            return memo[k][n]
        return dp(K, N)

    def superEggDrop(self, K, N):
        amax = 2 ** 31 - 1
        memo = [[amax] * (N + 1) for _ in range(K + 1)]

        def dp(k, n):
            if k == 0:
                return 0
            if k == 1:
                return n
            if n <= 1:
                return n
            if memo[k][n] != amax:
                return memo[k][n]
            left = 1
            right = n + 1
            while left < right:
                mid = left + (right - left) // 2
                broken = dp(k - 1, mid - 1)
                notbroken = dp(k, n - mid)
                if broken >= notbroken:
                    right = mid
                else:
                    left = mid + 1
            ans = 1 + max(dp(k - 1, left - 1), dp(k, n - left))
            memo[k][n] = ans
            return ans
        return dp(K, N)

    def superEggDrop2(self, K: int, N: int) -> int:
        memo = [[2 ** 31 - 1] * (N + 1) for _ in range(K + 1)]

        def dp(k, n):
            if k == 0:
                return 0
            if k == 1:
                return n
            if n <= 1:
                return n
            if memo[k][n] < 2 ** 31 - 1:
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

    def superEggDrop4(self, K, N):

        def f(x):
            ans = 0
            r = 1
            for i in range(1, K + 1):
                r *= x - i + 1
                r //= i
                ans += r
                if ans >= N:
                    break
            return ans
        (lo, hi) = (1, N)
        while lo < hi:
            mi = (lo + hi) // 2
            if f(mi) < N:
                lo = mi + 1
            else:
                hi = mi
        return lo
