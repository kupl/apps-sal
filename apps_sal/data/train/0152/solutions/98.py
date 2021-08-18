class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        if m == 2:
            return max(position) - min(position)
        position.sort()
        l, r = 1, (max(position) - min(position) + 1) // (m - 1)

        def helper(mindist):
            cnt = m - 1
            cur = min(position)
            for i in position[1:]:
                if i - cur >= mindist:
                    cur = i
                    cnt -= 1
                    if cnt == 0:
                        return True
            return False
        if helper(r):
            return r
        while l < r:
            mid = l + (r - l) // 2
            if helper(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1
