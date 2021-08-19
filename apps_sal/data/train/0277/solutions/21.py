class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        blue = right = 0
        for (i, a) in enumerate(light, 1):
            right = max(right, a)
            if i == right:
                blue += 1
        return blue
