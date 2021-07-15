class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ma,res,total = 0,0,0
        i = 0
        while i < len(s)-1:
            start = i
            while i < len(s)-1 and s[i+1] == s[i]:   #哪个在and前很重要
                i +=1
            end = i
            if start == end:
                i += 1
            else:
                for j in range(start, end+1):
                    ma = max(ma, cost[j])
                    total += cost[j]
                res += total-ma
                ma = 0
                total = 0
        return res
                
        
#         for i in range(len(s)-1):
#             if s[i+1] == s[i]:
#                 temp = min(cost[i],cost[i+1])
#                 res += temp
                
#         return res

