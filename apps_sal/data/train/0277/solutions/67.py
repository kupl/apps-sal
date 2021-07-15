class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        rolling_min = light[0]
        rolling_max = light[0]
        r = 0
        for i, l in enumerate(light):
            rolling_min = min(rolling_min, l)
            rolling_max = max(rolling_max, l)
            r += (rolling_min == 1 and rolling_max == i + 1)
        return r
