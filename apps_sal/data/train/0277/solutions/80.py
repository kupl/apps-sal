class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        curr_max = 0
        res = 0
        for idx, val in enumerate(light):
            curr_max = max(curr_max, val)
            if curr_max == idx + 1:
                res += 1
        return res
            
            

