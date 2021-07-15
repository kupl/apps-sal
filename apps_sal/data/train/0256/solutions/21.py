class Solution:
    def minEatingSpeed(self, array: List[int], hour: int) -> int:
        if len(array)==hour:
            return max(array)
        low=1
        high=max(array)
        ans=high
        while low<=high:
            mid=(low+high)//2
            h=hour
            for i in range(len(array)):
                if array[i]<=mid:
                    h-=1
                else:
                    if array[i]%mid==0:
                        h-=array[i]//mid
                    else:
                        h-=(array[i]//mid)+1
            if h>=0:
                ans =min(ans,mid)
                high=mid-1
            else:
                low=mid+1
        return ans

