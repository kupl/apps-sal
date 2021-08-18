class Solution:

    def allow(self, mid, position, m):
        balls = 1
        last = position[0]
        for i in range(1, len(position)):
            if(position[i] - last >= mid):
                balls += 1
                last = position[i]
        return balls >= m

    def maxDistance(self, position: List[int], m: int) -> int:
        o = Solution()
        position.sort()
        low = 0
        high = 1000000000
        pos = 0
        while(low <= high):
            mid = int((high + low) / 2)
            if(o.allow(mid, position, m)):
                low = mid + 1
                pos = mid
            else:
                high = mid - 1
        return pos
