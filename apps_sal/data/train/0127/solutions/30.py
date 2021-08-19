mod_ = 10 ** 9 + 7


class Solution:

    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        axis_group = G + 1
        axis_profit = P + 1
        n_profit = len(profit)
        mat = [[0 for p in range(axis_profit)] for g in range(axis_group)]
        mat[0][0] = 1
        for (pos, cur_profit) in enumerate(profit):
            cur_people = group[pos]
            for g in range(axis_group - 1, cur_people - 1, -1):
                for p in range(cur_profit + axis_profit - 1, cur_profit - 1, -1):
                    p2 = min(axis_profit - 1, p)
                    mat[g][p2] = (mat[g][p2] + mat[g - cur_people][p - cur_profit]) % mod_
        count = 0
        for row in mat:
            count = (count + sum(row[P:])) % mod_
        return count
