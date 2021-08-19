class Solution:

    def maxDistToClosest(self, seats) -> int:
        max_len = 0
        _cnt = 0
        for v in seats:
            if v == 0:
                _cnt += 1
            if v == 1:
                max_len = max(max_len, _cnt)
                _cnt = 0
        max_dist = (max_len + 1) // 2
        return max(max_dist, seats.index(1), seats[::-1].index(1))
