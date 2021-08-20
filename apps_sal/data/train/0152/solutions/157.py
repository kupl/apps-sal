class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def isPossible(mid, m):
            m -= 1
            i = 1
            prev = position[0]
            while i < n and m:
                if position[i] - prev >= mid:
                    prev = position[i]
                    m -= 1
                i += 1
            return m == 0
        position.sort()
        n = len(position)
        lo = hi = position[-1] - position[0]
        for i in range(n - 1):
            lo = min(lo, position[i + 1] - position[i])
        ans = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if isPossible(mid, m):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
