class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        l = 1
        r = max(piles)
        def findTime(count):
            hr = 0
            for p in piles: 
                hr += (p-1)//count+1
                if hr>H:
                    return False
            return True
        
        while l<r:
            mid = l+(r-l)//2
            if findTime(mid):
                r = mid
            else:
                l = mid+1
        return l
