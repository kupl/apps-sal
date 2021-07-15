class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        
        moments = 0 
        pair = [light[0], light[0] - 1]
        for i in range(1, len(light)):    
            if pair[1] == 0: 
                moments += 1
            
            if pair[0] > light[i]: 
                pair[1] -= 1
            else: 
                pair[1] = light[i] - pair[0] + pair[1] - 1
                pair[0] = light[i]
            
        if pair[1] == 0: 
            moments += 1
        
        return moments

