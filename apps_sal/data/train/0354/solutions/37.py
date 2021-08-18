class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0 for c in range(6)] for r in range(n)]
        for c in range(6):
            dp[0][c] = 1
        for r in range(1, n):
            for c in range(6):
                if r < rollMax[c]:
                    dp[r][c] = sum(dp[r - 1])
                else:
                    for prev in range(r - rollMax[c], r):
                        dp[r][c] += sum(dp[prev]) - dp[prev][c]
        return sum(dp[-1]) % 1000000007
