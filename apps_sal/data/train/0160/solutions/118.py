class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l = len(piles)
        dp = [[-1 for i in range(l)] for j in range(l)]

        def solve(piles, i, j, tot):
            alex = (j - i - l) % 2
            if i == j:
                if alex:
                    tot += piles[i]
                return tot > 0

            if dp[i][j] != -1:
                return dp[i][j]
            if alex:
                if solve(piles, i + 1, j, tot + piles[i]):
                    dp[i][j] = True
                    return True
                dp[i][j] = solve(piles, i, j - 1, tot + piles[j])
                return dp[i][j]
            else:
                if solve(piles, i + 1, j, tot - piles[i]):
                    dp[i][j] = True
                    return True
                dp[i][j] = solve(piles, i, j - 1, tot - piles[j])
                return dp[i][j]

        return solve(piles, 0, l - 1, 0)
