class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        m = 10 ** 9 + 7
        cur = [[0] * (G + 1) for _ in range(P + 1)]
        cur[0][0] = 1
        for p0, g0 in zip(profit, group):
            for p1 in range(P, -1, -1):
                for g1 in range(G, g0 - 1, -1):
                    cur[p1][g1] += cur[max(0, p1 - p0)][g1 - g0]

        return sum(cur[-1]) % m
