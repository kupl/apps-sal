class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def possible(d):
            cnt = 1
            cur = position[0]
            for i in range(1, len(position)):
                if position[i] - cur >= d:
                    cnt += 1
                    cur = position[i]
                if cnt >= m:
                    return True
            return False
        lo = 0
        hi = position[-1] - position[0]
        while lo < hi:
            mid = hi - (hi - lo) // 2
            if possible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
