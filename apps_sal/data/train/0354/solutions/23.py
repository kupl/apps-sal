class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        memo = [[0] * 7 for _ in range(n + 1)]
        for j in range(6):
            memo[1][j] = 1
            memo[1][-1] += memo[1][j]
        for i in range(2, n + 1):
            for j in range(6):
                memo[i][j] = memo[i - 1][-1]
                k = i - rollMax[j]
                if k == 1:
                    memo[i][j] -= 1
                elif k > 1:
                    memo[i][j] -= (memo[k - 1][-1] - memo[k - 1][j])
                memo[i][-1] += memo[i][j]
        return memo[n][6] % int(1e9 + 7)
