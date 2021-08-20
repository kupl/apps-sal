class Solution:

    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        count_dict = {}
        base = int(1000000000.0 + 7)
        for (groupi, profiti) in zip(group, profit):
            if groupi > G or groupi <= 0:
                continue
            tmp_dict = count_dict.copy()
            for ((groupj, profitj), count) in tmp_dict.items():
                if groupj + groupi <= G:
                    if profiti + profitj >= P:
                        count_dict[groupi + groupj, P] = count_dict.get((groupi + groupj, P), 0) + count % base
                    else:
                        count_dict[groupi + groupj, profiti + profitj] = count_dict.get((groupi + groupj, profiti + profitj), 0) + count % base
            if profiti >= P:
                count_dict[groupi, P] = count_dict.get((groupi, P), 0) + 1
            else:
                count_dict[groupi, profiti] = count_dict.get((groupi, profiti), 0) + 1
        out = 0
        for ((groupi, profiti), count) in count_dict.items():
            if profiti >= P:
                out += count
        return out % base
