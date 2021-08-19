class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def getBallCount(position, force):
            res, prev = 1, 0
            for i in range(1, len(position)):
                if position[i] - position[prev] >= force:
                    res += 1
                    prev = i
            return res

        # position.sort()
        # l,r,ans=0,position[-1],0
        # while l<=r:
        #     gap=l+(r-l)//2
        #     if getBallCount(position, gap) >= m:
        #         ans=gap
        #         l=gap+1
        #     else:
        #         r=gap-1
        # return ans

        position.sort()
        if m == 2:
            return position[-1] - position[0]
        l, r, res = 0, position[-1] + 1, 0
        while l < r:
            mid = l + (r - l) // 2
            # force is too small
            if getBallCount(position, mid) >= m:
                l = mid + 1
                res = mid
            else:
                r = mid
        # return res, not l.
        return res
