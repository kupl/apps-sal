class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        l, r = 1, position[-1] - position[0]
        res = r
        while l <= r:
            mid = (l + r) // 2
            prev, i, cnt = position[0], 1, m - 1
            while i < n and cnt > 0:
                if position[i] - prev >= mid:
                    cnt -= 1
                    prev = position[i]
                i += 1
            if cnt > 0:
                r = mid - 1
            else:
                res = mid
                l = mid + 1
        return res
