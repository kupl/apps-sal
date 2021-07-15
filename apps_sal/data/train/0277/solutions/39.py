class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = hi = on = 0
        for l in light:
            on += 1
            if l>hi:
                hi = l
            if on==hi:
                res+=1
        return res
            
            
            

