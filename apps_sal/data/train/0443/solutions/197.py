class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        teams_count = 0
        
        i = 0
        
        while i < len(rating)-2:
            j = i+1
            while j < len(rating) -1:
                k = j+1
                while k < len(rating):
                    if ((rating[i] < rating[j]) and (rating[j] < rating[k])) or ((rating[k] < rating[j]) and (rating[j] < rating[i])):
                        teams_count +=1
                 
                    k+=1
                j+=1
            i+= 1
            
        return teams_count
            
                    
                
            

