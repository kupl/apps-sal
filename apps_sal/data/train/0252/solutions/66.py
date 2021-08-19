class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        if len(ranges) == 0:
            return 0
        segments = [(max(0, index - num), min(n, index + num)) for (index, num) in enumerate(ranges)]
        segments = sorted(segments)
        (left, right) = (-1, 0)
        cnt = 0
        for (a, b) in segments:
            if a > right:
                break
            if right == n:
                break
            if right >= a > left:
                cnt += 1
                left = right
            right = max(right, b)
        if right == n:
            return cnt
        return -1
