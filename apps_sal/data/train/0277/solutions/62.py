class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        right = res = 0
        for i, v in enumerate(light):
            right = max(right, v)
            res += right == i + 1
        return res
