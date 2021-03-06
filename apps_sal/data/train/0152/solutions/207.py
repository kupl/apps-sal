class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lo = 1
        hi = position[-1] - position[0]

        def count(dis):
            res = 1
            i = 0
            curr = 0
            while i < len(position):
                if position[i] - position[curr] >= dis:
                    res += 1
                    curr = i
                i += 1
            return res
        while lo < hi:
            mid = hi - (hi - lo) // 2
            if count(mid) >= m:
                lo = mid
            else:
                hi = mid - 1
        return lo
