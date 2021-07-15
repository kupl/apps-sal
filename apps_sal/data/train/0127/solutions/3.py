class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        memo = [[0] * (G + 1) for _ in range(P + 1)]
        memo[0][0] = 1
        for p, g in zip(profit, group):
            for i in reversed(range(P + 1)):
                for j in reversed(range(G + 1 - g)):
                    memo[min(i + p, P)][j + g] += memo[i][j]
        return sum(memo[-1]) % (10 ** 9 + 7)
