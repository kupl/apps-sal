class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = nums_on = last_pos = 0
        for pos in light:
            nums_on += 1
            if pos > last_pos:
                last_pos = pos
            if nums_on == last_pos:
                res += 1
                
        return res
