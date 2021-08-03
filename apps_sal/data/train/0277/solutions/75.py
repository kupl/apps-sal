class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        maxv = 0
        result = 0

        for i, num in enumerate(light):
            maxv = max(maxv, num)
            if maxv == i + 1:
                result += 1
        return result
