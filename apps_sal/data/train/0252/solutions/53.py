class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        steps = [0] * (n + 1)
        for (i, r) in enumerate(ranges):
            if i - r < 0:
                steps[0] = max(i + r, steps[0])
            else:
                steps[i - r] = max(i + r, steps[i - r])
        num = 1
        cur = 0
        cur_max = steps[0]
        while cur_max < n:
            next_max = cur_max
            for loc in range(cur + 1, cur_max + 1):
                next_max = max(next_max, steps[loc])
            if next_max == cur_max:
                return -1
            num += 1
            cur = cur_max
            cur_max = next_max
        return num
