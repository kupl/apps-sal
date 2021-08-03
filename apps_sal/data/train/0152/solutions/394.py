class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(dist, m):
            last = position[0]
            for i in range(1, len(position)):
                if(position[i] - last >= dist):
                    m -= 1
                    last = position[i]
            return(m <= 1)
        l = 0
        r = position[-1] - position[0]
        while(l < r):
            mid = l + ((r - l + 1) >> 1)
            if(check(mid, m)):
                l = mid
            else:
                r = mid - 1
        return(l)
