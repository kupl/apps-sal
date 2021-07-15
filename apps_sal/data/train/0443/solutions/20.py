class Solution:
    def numTeams(self, rating: List[int]) -> int:
        numT = 0 
        
        if (len(rating) < 3): 
            return 0 
        
        blah = list(range(len(rating)))
        
        for first_idx in blah[:-2]:
            first = rating[first_idx]

            for second_idx in blah[first_idx:]:
                second = rating[second_idx]
                
                for third_idx in blah[second_idx:]:
                    third = rating[third_idx]
                    if (first < second and second < third):
                        numT += 1
                    if (first > second and second > third):
                        numT += 1
                        
        return numT

