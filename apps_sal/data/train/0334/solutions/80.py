class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        output=0
        s = list(s)
        i=0
        while i  < (len(s)-1):
            if s[i] ==s[i+1]:
                
                if i == len(s)-2:
                    output += min(cost[i],cost[i+1])
                else:
                    j=i+2
                    
                    while s[i] ==s[j] and j < len(s)-1:
                        #print(j)
                        j+=1
                    
                    print(cost[i:j])
                   
                    
                    if s[-1]!=s[-2]:
                        output =output + sum(cost[i:j]) - max(cost[i:j])
                    
                    elif j == len(s)-1:
                        output =output + sum(cost[i:j+1]) - max(cost[i:j+1])
                    else:
                        output =output + sum(cost[i:j]) - max(cost[i:j])
                    i=j-1
            i+=1
                
        return output
