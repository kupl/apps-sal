class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        N = len(people)
        num_boats = 0
        
        if len(people) == 1:
            return 1
        
        less_than_half = [p for p in people if p <= limit/2]
        more_than_half = [p for p in people if p > limit/2]
        
        while len(more_than_half) > 0 and len(less_than_half) > 0:            
            
            if more_than_half[-1] + less_than_half[0] > limit:
                # largest doesn't fit with smallest
                more_than_half.pop(-1)
                num_boats += 1
                continue
                
            else:
                # largest fit with smallest
                more_than_half.pop(-1)
                less_than_half.pop(0)
                num_boats += 1
                continue      
                
        # no more pairings - one of the lists is empty
        num_boats += len(more_than_half)
        num_boats += int(len(less_than_half)/2 +0.5)            
                
        return num_boats
