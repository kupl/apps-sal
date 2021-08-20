class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        max_so_far = 0
        ret = 0
        for (i, l) in enumerate(light):
            max_so_far = max(max_so_far, l)
            ret += max_so_far == i + 1
        return ret
