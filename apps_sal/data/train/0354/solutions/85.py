class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 7 for _ in range(n+1)]
        dp[1][1:] = [1] * 6
        for i in range(2, n+1):
            for j in range(1, 7):
                for k in range(1, rollMax[j-1]+1):
                    if i-k < 0:
                        break
                    elif i-k == 0:
                        dp[i][j] += 1
                    else:
                        dp[i][j] += sum([dp[i-k][l] for l in range(1, 7) if l != j])
        return sum(dp[-1]) % (10**9+7)

