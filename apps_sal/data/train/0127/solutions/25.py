class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        m = 10**9 + 7
        table = [[0] * (G + 1) for _ in range(P + 1)]
        table[0][0] = 1
        # table[p][g] to index

        for g, p in zip(group, profit):
            for pi in range(P, -1, -1):
                for gi in range(G - g, -1, -1):
                    new_pi = min(P, pi + p)
                    table[new_pi][gi + g] = (table[new_pi][gi + g] + table[pi][gi]) % m

        total = 0
        for x in table[P]:
            total = (total + x) % m

        return total
