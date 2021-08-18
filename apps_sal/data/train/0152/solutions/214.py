class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lo, hi = 1, (position[-1] - position[0]) // (m - 1) + 1
        res = 0

        def possible(gap):
            balls = m
            prev = None
            for i in range(len(position)):
                if not prev:
                    prev = position[i]
                    balls -= 1
                else:
                    if abs(prev - position[i]) < gap:
                        continue
                    else:
                        prev = position[i]
                        balls -= 1
            if balls <= 0:
                return True
            return False

        while lo <= hi:
            mid = (lo + hi) // 2

            if possible(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return res
