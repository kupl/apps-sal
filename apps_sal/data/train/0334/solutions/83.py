class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ss = list(s)
        tot_cost = 0
        i = 0
        while i < len(ss) - 1:
            if ss[i] == ss[i+1]:
                start_i = i
                end_i = i+1
                while end_i < len(ss) - 1 and ss[end_i] == ss[end_i + 1]:
                    end_i += 1
                dup_sum = sum(cost[start_i:end_i+1])
                dup_max = max(cost[start_i:end_i+1])
                tot_cost += dup_sum - dup_max
                i = end_i
            i += 1
        
        return tot_cost
