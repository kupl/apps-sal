class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        maximum = 1
        res = 0
        for (i, val) in enumerate(light):
            maximum = max(maximum, val)
            if i + 1 == maximum:
                res += 1
        return res
