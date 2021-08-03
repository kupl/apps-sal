class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = 0
        right = 0

        for idx in range(len(light)):
            right = max(right, light[idx])

            if right == idx + 1:
                res += 1

        return res
