class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = 0
        
        
        #Get the first element at rating[base]
        for base in range(len(rating)):
            second = base + 1
            
            while second  < len(rating):
                #If the second element is greater than the first, look for the third after that position
                if rating[second] > rating[base]:
                    third = second + 1
                    
                    while third < len(rating):
                        if rating[third] > rating[second]:
                            teams += 1
                    
                        #print(base, second, third, rating[base], rating[second], rating[third])
                        third += 1
                    
                second += 1
        
        for base in range(len(rating)):
            second = base + 1
            
            while second < len(rating):
                
                if rating[second] < rating[base]:
                    third = second + 1
                    
                    while third < len(rating):
                        if rating[third] < rating[second]:
                            teams += 1
                        
                        third += 1
                second += 1
                
        return teams
