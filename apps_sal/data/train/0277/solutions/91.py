class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = 0
        high = 0
        on = 0

        for l in light:
            on += 1
            if l > high:
                high = l
            if on == high:
                res += 1

        return res
