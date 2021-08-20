class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        count = 0
        right = 0
        for i in range(len(light)):
            right = max(light[i], right)
            if right == i + 1:
                count += 1
        return count
