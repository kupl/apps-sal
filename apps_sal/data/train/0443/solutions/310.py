class Solution:
    def numTeams(self, rating: List[int]) -> int:
        c = 0
        for i in range(len(rating)):
            j = i + 1
            while(j<len(rating)):
                k= j + 1
                while(k<len(rating)):    
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        c += 1
                    k += 1
                
                j += 1
        
        return c
                        
            

