class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def valid(dis):
            count = 1
            prev = position[0]
            for n in position:
                if n - prev >= dis:
                    count += 1
                    prev = n
                if count == m:
                    return True
            return False
        (l, r) = (0, position[-1])
        ret = 0
        while l < r:
            mid = l + (r - l) // 2
            if valid(mid):
                ret = max(ret, mid)
                l = mid + 1
            else:
                r = mid
        return ret
