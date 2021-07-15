class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if len(piles)==H:
            return max(piles)
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            h=H
            for i in range(len(piles)):
                if piles[i]<=mid:
                    h-=1
                else:
                    if piles[i]%mid==0:
                        h-=piles[i]//mid
                    else:
                        h-=(piles[i]//mid)+1
            if h>=0:
                ans =min(ans,mid)
                high=mid-1
            else:
                low=mid+1
        return ans
