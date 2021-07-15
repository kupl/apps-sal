class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if not s:
            return 0
        last = s[0]
        i = 0
        res = 0
        while i < len(s) - 1:
            if s[i] == s[i+1]:
                j = i + 1
                sums = cost[i]
                maxs = cost[i]
                while j <len(s) and s[j] == s[j-1]:
                    sums += cost[j]
                    maxs = max(maxs, cost[j])
                    j += 1
                    
                #print(i,j)
                res += sums - maxs
                i = j
                
            else:
                i += 1
        return res
                

