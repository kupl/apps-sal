class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l = max(1,sum(piles)//H)
        r = max(piles)//(H//len(piles)) + 1
        # print(l,r)
        def hours(rate):
            count = 0
            for x in piles:
                count += (x+rate-1)//rate
            return count
                
        while l <= r:
            mid = (l+r)//2
            h = hours(mid)
            if h > H:
                l = mid+1
            else:
                ans = mid
                r = mid-1
        return ans   
