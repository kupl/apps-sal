class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        right = -1
        res = 0
        for i in range(len(light)):
            right = max(light[i], right)
            if right == i + 1:
                res += 1
        return res
