class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        ranges = [[i - val, i + val] for (i, val) in enumerate(ranges)]
        ranges.sort()
        print(ranges)
        max_reach = 0
        i = 0
        taps = 0
        while max_reach < n:
            curr_reach = 0
            if max_reach == 6:
                print(3)
            while i < n + 1 and ranges[i][0] <= max_reach:
                curr_reach = max(curr_reach, ranges[i][1])
                i += 1
            print(curr_reach, max_reach)
            if curr_reach <= max_reach:
                return -1
            max_reach = curr_reach
            taps += 1
        return taps
