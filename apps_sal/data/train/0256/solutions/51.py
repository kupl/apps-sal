class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def valid(mid):
            if mid==0:
                return False
            hours = 0
            for i in piles:
                if i<mid:
                    hours+=1
                else:
                    hours+=math.ceil(i/mid)

            return hours<=H
        
        if not piles:
            return 0
        
        piles = sorted(piles)
        s,e = 0,sum(piles)
        ans = -1
        while s<=e:
            mid = (s+e)//2
            if valid(mid):
                ans = mid
                e = mid-1
            else:
                s = mid+1
                
        return ans

