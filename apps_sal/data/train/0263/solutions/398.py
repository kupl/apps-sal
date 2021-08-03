class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        hash_map = {0: (4, 6), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (0, 3, 9), 5: (), 6: (0, 1, 7), 7: (2, 6), 8: (1, 3), 9: (2, 4)}

        dp = {}

        def ways_n(n, val):
            if n == 0:
                return 1

            if (n, val) in dp:
                return dp[n, val]

            dp[n, val] = 0
            for i in hash_map[val]:
                dp[n, val] += ways_n(n - 1, i)
            return dp[n, val]

        ans = 0
        for i in range(10):
            ans += ways_n(n - 1, i)
        return ans % (10**9 + 7)
