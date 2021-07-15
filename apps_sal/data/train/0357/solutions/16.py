class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        '''
        [1,0,0,0,1,0,1]
        
        left = [0,0,0,0,4,4,6]
        right [0,4,4,4,4,6,6]
        
        '''
        
        
        n = len(seats)
        left, right = [n] * len(seats), [n] * len(seats)
            
        for i in range(0, len(seats)):
            if seats[i] == 1:
                left[i] = 0 
            elif i > 0 and seats[i] == 0:
                left[i] =  left[i-1] + 1 
            
        for i in range(len(seats)-1, -1, -1):
            if seats[i] == 1:
                right[i] = 0 
            elif i < len(seats) - 1 and seats[i] == 0:
                right[i] = right[i+1] + 1 

        maxDistance = float('-inf')
        for i, seat in enumerate(seats):
            if seat == 0:
                maxDistance = max(maxDistance, min(left[i], right[i]))
        return maxDistance
