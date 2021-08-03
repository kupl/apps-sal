class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        min_costs = {}
        cut_set = set(cuts)

        def find_min_cost(start: int, end: int):
            if (start, end) in min_costs:
                return min_costs[(start, end)]
            cuts_in = []
            for i in cut_set:
                if i > start and i < end:
                    cuts_in.append(i)
            if len(cuts_in) == 0:
                min_costs[(start, end)] = 0
                return 0
            if len(cuts_in) == 1:
                min_costs[(start, end)] = end - start
                return end - start
            result = len(cuts_in) * (end - start)
            for cut in cuts_in:
                subresult = end - start
                subresult += find_min_cost(start, cut)
                subresult += find_min_cost(cut, end)
                if subresult < result:
                    result = subresult
            min_costs[(start, end)] = result
            return result

        return find_min_cost(0, n)
