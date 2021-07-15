class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        s = s+'#'
        totalcost = 0
        idx = 1
        while idx<len(s):
            if s[idx] == s[idx-1]:
                start = idx-1
                end = idx
                idx +=1
                
                while idx<len(s):
                    
                    if s[idx]!=s[idx-1]:
                        end = idx-1
                        break
                    else:
                        idx+=1
                 
                
                
                print((start,end))
                totalcost +=sum(cost[start:end+1])-max(cost[start:end+1])
            else:
                idx +=1
        return totalcost
            
            
                
                    
            
              
                    

