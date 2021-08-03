class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        lo = 1
        hi = position[-1] - position[0]
        res = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            count = 1
            prev = position[0]
            for i in range(1, n):
                if position[i] - prev >= mid:
                    count += 1
                    prev = position[i]

            if count >= m:
                res = max(res, mid)
                lo = mid + 1
            else:
                hi = mid - 1
        return res
