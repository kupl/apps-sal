class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lo, hi = 0, position[-1] - position[0]

        def possible(target, m):
            idx = prev = 0
            while m:
                if idx >= len(position):
                    return False
                if not prev or position[idx] >= prev + target:
                    m -= 1
                    prev = position[idx]
                else:
                    idx += 1
            return True

        while lo <= hi:
            mid = (lo + hi) >> 1
            if possible(mid, m):
                lo = mid + 1
            else:
                hi = mid - 1

        return lo - 1
