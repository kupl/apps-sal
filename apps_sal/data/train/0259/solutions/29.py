class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def thres(div):
            return sum([ceil(val/div) for val in nums])
        
        l,h=1,max(nums)
        
        while(l<=h):
            mid=l+((h-l)>>1)
            if thres(mid)<=threshold: h=mid-1
            else: l=mid+1
        
        return l

