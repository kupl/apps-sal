class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        pre_s = [0]
        acc = 0
        for num in piles:
            acc += num
            pre_s.append(acc)
        m = len(piles)
        dp = [[0] * m for _ in range(m)]
        for i in reversed(list(range(m))):
            for j in range(i, m):
                if i == j:
                    dp[i][j] = piles[i]
                else:
                    s = pre_s[j + 1] - pre_s[i]
                    if dp[i + 1][j] < dp[i][j - 1]:
                        dp[i][j] = s - dp[i + 1][j]
                    else:
                        dp[i][j] = s - dp[i][j - 1]
        return dp[0][-1] > dp[1][-1] or dp[0][-1] > dp[0][-2]
