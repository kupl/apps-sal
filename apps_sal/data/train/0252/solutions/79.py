class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i, r in enumerate(ranges):
            intervals.append((i - r if i - r > 0 else 0, i + r))

        intervals.sort(key=lambda t: (t[0], -t[1]))
        l = len(intervals)

        i = 0
        ans = 1
        while i < l:
            if intervals[i][1] >= n:
                return ans
            right = -1
            next_i = -1
            for j in range(i + 1, l):
                if intervals[j][0] <= intervals[i][1] and intervals[j][1] >= right:
                    right = intervals[j][1]
                    next_i = j

            if next_i == -1:
                return -1

            ans += 1
            i = next_i

        return ans
