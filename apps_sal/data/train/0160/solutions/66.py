class Solution:

    def stoneGame(self, piles):
        n = len(piles)
        memo = dict()

        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[i, j]
            ans = max(piles[i] - dp(i + 1, j), piles[j] - dp(i, j - 1))
            memo[i, j] = ans
            return ans
        return dp(0, n - 1) > 0

    def stoneGame1(self, piles):
        n = len(piles)
        memo = dict()

        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[i, j]
            if (j - i + n) % 2 == 1:
                ans = max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:
                ans = min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))
            memo[i, j] = ans
            return ans
        return dp(0, n - 1) > 0

    def stoneGame2(self, piles):
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for alen in range(2, n + 1):
            for i in range(0, n - alen + 1):
                j = i + alen - 1
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][n - 1] > 0

    def stoneGame3(self, piles):
        n = len(piles)
        memo = dict()

        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[i, j]
            ans = max(piles[i] - dp(i + 1, j), piles[j] - dp(i, j - 1))
            memo[i, j] = ans
            return ans
        return dp(0, n - 1) > 0

    def stoneGame4(self, piles):
        return True

    def stoneGame3(self, piles):
        n = len(piles)
        dp = [0] * n
        for alen in range(2, n + 1):
            for i in range(0, n - alen + 1):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + alen - 1] - dp[i])
        return dp[0] > 0

    def stoneGame2(self, piles):
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for alen in range(2, n + 1):
            for i in range(0, n - alen + 1):
                j = i + alen - 1
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][n - 1] > 0

    def stoneGame1(self, piles: List[int]) -> bool:
        dp = dict()

        def score(piles, l, r):
            if (l, r) in dp:
                return dp[l, r]
            if l == r:
                dp[l, r] = piles[l]
                return piles[l]
            res = max(piles[l] - score(piles, l + 1, r), piles[r] - score(piles, l, r - 1))
            dp[l, r] = res
            return res
        res = score(piles, 0, len(piles) - 1)
        return True if res > 0 else False
