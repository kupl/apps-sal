class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        res = right = 0
        for (i, n) in enumerate(light):
            right = max(right, n)
            res += 1 if right == i + 1 else 0
        return res
