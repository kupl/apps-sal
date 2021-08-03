import bisect


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        n = len(position)
        if m == 2:
            return position[-1] - position[0]

        lp = 0
        rp = (position[-1] - position[0])

        def can(gap):
            lidx = 0
            left = m - 1
            ptr = 1
            while left > 0 and ptr < n:
                if position[ptr] - position[lidx] >= gap:
                    left -= 1
                    lidx = ptr
                    ptr = lidx + 1
                    continue
                ptr += 1
            return left == 0

        ans = 0
        while lp < rp:
            mid = (lp + rp + 1) // 2
            if can(mid):
                lp = mid
            else:
                rp = mid - 1
        return lp
