class Solution:
    def recur(self, i, j, piles, n, dp, s):
        if j == i + 1:
            return max(piles[i], piles[j])
        if dp[i + 1][j] != -1:
            l = dp[i + 1][j]
        else:
            l = self.recur(i + 1, j, piles, n, dp, s - piles[i])
        if dp[i][j - 1] != -1:
            r = dp[i][j - 1]
        else:
            r = self.recur(i, j - 1, piles, n, dp, s - piles[j])

        ans = max(s - l, s - r)
        dp[i][j] = ans
        return ans

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[-1 for i in range(n + 1)] for j in range(n + 1)]
        m = (self.recur(0, n - 1, piles, n, dp, sum(piles)))

        if m > sum(piles) - m:
            return True
        else:
            return False
