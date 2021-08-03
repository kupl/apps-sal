class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        farthestRightAt = [-1] * (n + 1)
        for i, r in enumerate(ranges):
            if r == 0:
                continue
            left = i - r
            right = i + r
            for j in range(max(0, left), min(right + 1, n + 1)):
                farthestRightAt[j] = min(n, max(farthestRightAt[j], right))

        if -1 in farthestRightAt:
            return -1
        i = 0
        count = 0
        while i < n:
            i = farthestRightAt[i]
            count += 1
        return count
