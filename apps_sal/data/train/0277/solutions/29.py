class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        right = result = 0
        for i, a in enumerate(light, 1):
            right = max(right, a)
            result += right == i
        return result
