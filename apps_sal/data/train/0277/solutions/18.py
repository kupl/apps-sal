class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        count = 0
        right = 0
        target = 0
        for n in reversed(light):
            right += 1
            target = max(target, len(light) - n + 1)
            if right == target:
                count += 1
        return count
