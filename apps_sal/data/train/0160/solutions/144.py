# 877. Stone Game

# It's tricky when we have even number of piles of stones.
# You may not have this condition in an interview.

# Follow-up:

# What if piles.length can be odd?
# What if we want to know exactly the diffenerce of score?
# Then we need to solve it with DP.

# dp[i][j] means the biggest number of stones
# you can get more than opponent picking piles in piles[i] ~ piles[j].
# You can first pick piles[i] or piles[j].

# If you pick piles[i], your result will be piles[i] - dp[i + 1][j]
# If you pick piles[j], your result will be piles[j] - dp[i][j - 1]
# So we get:
# dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
# We start from smaller subarray and then we use that to calculate bigger subarray.

# Note that take evens or take odds, it's just an easy strategy
# to win when the number of stones is even.
# It's not the best solution!
# I didn't find a tricky solution when the number of stones is odd (maybe there is).

class Solution1:  # 2D DP
    def stoneGame(self, piles: List[int]) -> bool:
        p = piles
        n = len(p)

        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = p[i]

        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])

        return dp[0][-1] > 0


class Solution:  # 1D DP, Space: O(N)
    def stoneGame(self, p):
        n = len(p)
        dp = p[:]
        for d in range(1, n):
            for i in range(n - d):
                # 这次拿完会赢，下次？？？？
                dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
        return dp[0] > 0
