class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[1] * 6 for _ in range(n)]
        # dp[i][j]代表长度为i的序列，结尾为j的组合数目
        # 得到所有组合减去不符合规则的
        for i in range(1, n):
            for j in range(6):
                dp[i][j] = sum(dp[i - 1])
                if i == rollMax[j]:  # 此时连着有j项
                    dp[i][j] -= 1
                if i > rollMax[j]:
                    for k in range(6):
                        if k != j:
                            dp[i][j] -= dp[i - 1 - rollMax[j]][k]
        return sum(dp[-1]) % (10**9 + 7)
