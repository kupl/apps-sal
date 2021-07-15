from heapq import heapify,heappush,heappop
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        h = []
        for i in range(len(nums)):
            heappush(h,(nums[i],i))
        ans=0
        for k in range(1,right+1):
            x,i=heappop(h)
            if k>=left:
                ans+=x
            if i+1<len(nums):
                heappush(h,(x+nums[i+1],i+1))
        return ans%(10**9+7)
