class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = 0
        highest = 0
        ans = 0

        for bulb in light:
            n += 1
            highest = max(highest, bulb)
            if highest == n:
                ans += 1

        return ans
