class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def check(d):
            k, pre = 1, position[0]
            for i in range(1, n):
                if position[i] - pre >= d:
                    k += 1
                    pre = position[i]
            return k >= m

        lo, hi = 0, position[-1] - position[0]
        while lo < hi:
            mid = hi - (hi - lo) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
