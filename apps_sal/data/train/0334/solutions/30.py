class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        #greedy
        target = s[0]
        cost_list = [cost[0]]
        res = 0
        for i in range(1, len(cost)):
          if s[i] == target:
            cost_list.append(cost[i])
          else:
            if len(cost_list) >= 2: res += sum(cost_list) - max(cost_list)
            cost_list = [cost[i]]
            target = s[i]
        if len(cost_list) >= 2: res += sum(cost_list) - max(cost_list)
        return res
        
            

