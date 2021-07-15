class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        # print(\"===\")
        repeating=[]
        last=None
        ans=0
        for i,c in enumerate(s):
            # print(\"processing\",c)
            if c!=last:
                last=c
                if len(repeating)>1:
                    cost_win=cost[i-len(repeating):i]
                    spent = sum(cost_win)-max(cost_win)
                    # print(spent)
                    ans+=spent
                
                repeating= [c]
            
            else:
                repeating.append(c)
                
        if len(repeating)>1:
            cost_win=cost[len(s)-len(repeating):]
            spent = sum(cost_win)-max(cost_win)
            # print(spent)
            ans+=spent
        return ans
