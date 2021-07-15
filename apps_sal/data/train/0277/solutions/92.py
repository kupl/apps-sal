class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        # count times when all the lights on the left are on
        # which is: when the max idx of the lights on == the the number of lights on. 
        max_idx = float('-inf')
        cnt = 0
        for i in range(len(light)):
            max_idx = max(max_idx, light[i])
            if max_idx == i + 1:
                cnt += 1
        return cnt
        
            

