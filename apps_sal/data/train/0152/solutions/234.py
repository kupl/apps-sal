class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()
        n = len(pos)
        if m == 2:
            return pos[-1] - pos[0]

        def valid(k):
            count, cur = 1, pos[0]
            for p in pos[1:]:
                if p - cur >= k:
                    count += 1
                    cur = p
            return count >= m

        l, r = 0, pos[-1] - pos[0]
        ans = 0
        while l < r:
            mid = (l + r) // 2
            if valid(mid):
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid
        return ans
