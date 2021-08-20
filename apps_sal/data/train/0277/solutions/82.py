class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        max_on = 0
        count = 0
        for (idx, bulb) in enumerate(light):
            max_on = max(max_on, bulb)
            if max_on == idx + 1:
                count += 1
        return count
