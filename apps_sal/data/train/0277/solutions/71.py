class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        right = res = 0
        for (i, a) in enumerate(light, 1):
            right = max(right, a)
            res += right == i
        return res
