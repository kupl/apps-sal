class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        inner_array = []
        outer_array = []
        consecutive = False
        for (i, val) in enumerate(zip(s, cost)):
            if i == len(cost) - 1:
                break
            else:
                char = val[0]
                c = val[1]
                if char == s[i + 1]:
                    if consecutive:
                        inner_array.append(cost[i + 1])
                    else:
                        inner_array.append(c)
                        inner_array.append(cost[i + 1])
                        consecutive = True
                    if i == len(cost) - 2:
                        outer_array.append(inner_array)
                else:
                    consecutive = False
                    if inner_array:
                        outer_array.append(inner_array)
                        inner_array = []
        res = 0
        for i in outer_array:
            res += sum(sorted(i)[:-1])
        return res
