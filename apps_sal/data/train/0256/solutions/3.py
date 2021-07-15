import math
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def helper(k):
            ret=0
            for pile in piles:
                ret+=math.ceil(pile/k)
                if ret>H:
                    return False
            return True
        l,r=1,max(piles)
        while l<=r:
            mid=l+(r-l)//2
            if helper(mid):
                r=mid-1
            else:
                l=mid+1
        return l

