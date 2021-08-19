class Solution:

    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        dp = [[[0 for _ in range(G + 1)] for _ in range(P + 1)] for _ in range(len(group) + 1)]
        dp[0][0][0] = 1
        for i in range(1, len(group) + 1):
            for p in range(P + 1):
                for g in range(G + 1):
                    dp[i][p][g] += dp[i - 1][p][g]
                    if g + group[i - 1] < G + 1:
                        dp[i][min(p + profit[i - 1], P)][g + group[i - 1]] += dp[i - 1][p][g]
        return sum([dp[len(group)][P][g] for g in range(1, G + 1)]) % (10 ** 9 + 7)
