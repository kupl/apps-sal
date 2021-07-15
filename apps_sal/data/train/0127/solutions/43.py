class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        Cnt = 0
        dp_ = [[0] * ( G + 1 ) for _ in range( P + 1)]
        dp_[0][0] = 1
        for i in range(1, len(group) + 1):
            for p in range(P, - 1, -1):
                for v in range(G-group[i-1], -1, -1):
                    dp_[min(p + profit[i-1], P)][v+group[i-1]] = (dp_[p][v] + dp_[min(p + profit[i-1], P)][v+group[i-1]])%MOD
        return sum(dp_[P])%MOD
