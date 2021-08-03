class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        dp = [[2500001] * (n + 1) for _ in range(n + 1)]

        def kmp(i, j):
            if i > j:
                return 0
            elif dp[i][j] != 2500001:
                return dp[i][j]
            else:

                parity = (j - i + 1) % 2
                if parity == 1:
                    dp[i][j] = min(-piles[i] + kmp(i + 1, j), -piles[j] + kmp(i, j - 1))
                    return dp[i][j]
                else:
                    dp[i][j] = max(piles[i] + kmp(i + 1, j), piles[j] + kmp(i, j - 1))
                    return dp[i][j]
        return kmp(0, n - 1) > 0
