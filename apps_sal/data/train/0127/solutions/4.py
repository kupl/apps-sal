class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        memo = [[0] * (G + 1) for _ in range(P + 1)]
        memo[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    memo[min(P, p + i)][j + g] += memo[i][j]
        return sum(memo[P]) % (10**9 + 7)
