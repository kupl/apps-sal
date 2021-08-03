class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        cum_map = {
            0: -1,
        }
        intervals = [-1] * len(nums)
        cur = 0
        for i, x in enumerate(nums):
            cur += x
            rest = cur - target
            boundary = cum_map.get(rest)
            if boundary is not None:
                intervals[i] = boundary + 1
            cum_map[cur] = i

        res = 0
        s = [0] * len(nums)
        for i in range(len(nums)):
            if intervals[i] == i:
                s[i] = s[i - 1] + 1
                continue

            s[i] = s[i - 1]
            if intervals[i] == 0:
                s[i] = max(s[i - 1], 1)
            elif intervals[i] > 0:
                s[i] = max(s[i - 1], s[intervals[i] - 1] + 1)

        return s[-1]
