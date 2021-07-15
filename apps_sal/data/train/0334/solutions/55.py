class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        sums = 0
        max_cost = 0
        ans = 0
        flag = False
        
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                sums += cost[i-1]
                flag = True
                if max_cost < cost[i-1]:
                    max_cost = cost[i-1]
            else:
                if flag:
                    if max_cost < cost[i-1]:
                        max_cost = cost[i-1]
                    sums += cost[i-1]
                    ans += sums - max_cost
                    # print(ans, sums, max_cost)
                sums = 0
                flag = False
                max_cost = 0
        
        if flag:
            if max_cost < cost[-1]:
                max_cost = cost[-1]
            sums += cost[-1]
            ans += sums - max_cost
            # print(ans, sums, max_cost)
                
        return ans
