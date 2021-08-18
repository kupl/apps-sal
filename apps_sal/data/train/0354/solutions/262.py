class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[1 for _ in range(6)] for _ in range(n)]

        for i in range(1, n):
            for j in range(6):
                inc = sum(dp[i - 1])
                prev = i - rollMax[j] - 1
                if prev == -1:
                    inc -= 1
                elif prev >= 0:
                    for k in range(6):
                        if k == j:
                            continue
                        inc -= dp[prev][k]
                dp[i][j] = inc
        return sum(dp[-1]) % (10 ** 9 + 7)
