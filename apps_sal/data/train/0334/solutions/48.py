class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        cur =0
        mycost = 0
        while cur < len(s)-1:
            if s[cur] == s[cur+1]:
                temp=[]
                letter = s[cur]
                while cur < len(s) and s[cur] == letter:
                    temp.append(cost[cur]) 
                    cur +=1
                mycost += sum(temp) - max(temp)
            else:
                cur+=1
                
        return mycost
