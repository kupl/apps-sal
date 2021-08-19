class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        (min_seen, max_seen) = (float('inf'), float('-inf'))
        times = 0
        for (i, moment) in enumerate(light):
            min_seen = min(min_seen, moment)
            max_seen = max(max_seen, moment)
            times += max_seen - min_seen == i and min_seen == 1 and (max_seen == i + 1)
        return times
