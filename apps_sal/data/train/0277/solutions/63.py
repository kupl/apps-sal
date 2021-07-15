class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        max_v = 0
        res = 0
        
        for i,v in enumerate(light):
            max_v = max(max_v, v)
            if max_v == i+1:
                res += 1
        
        return res
