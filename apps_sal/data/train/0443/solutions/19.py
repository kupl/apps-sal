class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        incr = True
        for i in range(len(rating)-1):
                
            for j in range(i+1, len(rating)):
                if rating[i] < rating[j]: incr = True
                elif rating[i] > rating[j]: incr = False
                else: continue
                    
                for k in range(j+1, len(rating)):
                    if ((rating[j] < rating[k] and incr) or 
                        (rating[j] > rating[k] and not incr)):
                            count += 1
        
        return count
