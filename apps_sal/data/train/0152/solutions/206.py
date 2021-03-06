import bisect


class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)

        def possible(gap):
            prev = position[0]
            idx = 0
            left = m - 1
            while left > 0:
                idx = bisect.bisect_left(position, prev + gap, idx + 1, n)
                if idx >= n:
                    return False
                else:
                    prev = position[idx]
                    left -= 1
            return True
        position.sort()
        min_gap = 1
        max_gap = position[-1] - position[0]
        while min_gap <= max_gap:
            cur_gap = (min_gap + max_gap) // 2
            if possible(cur_gap):
                min_gap = cur_gap + 1
            else:
                max_gap = cur_gap - 1
        return min_gap - 1
