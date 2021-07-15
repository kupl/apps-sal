class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        if m == 2: return position[-1] - position[0]
        l, r = 1, position[-1]
        ans = 0
        while l < r:
            mid = (l + r) // 2
            prev, balls = -1000000000, 0
            for p in position:
                if p - prev >= mid:
                    balls += 1
                    if balls == m: break
                    prev = p
            if balls == m:
                ans = mid
                l = mid + 1
            else:
                r = mid
        return ans
