class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp=[-sys.maxsize]*len(nums)
        ans=nums[0]
        dp[0]=nums[0]
        heap=[(-nums[0],0)]
        heapq.heapify(heap)
        for i in range(1,len(nums)):
            bound=i-k
            while heap[0][1]<bound:
                heapq.heappop(heap)
            dp[i]=max(dp[i],nums[i],-heap[0][0]+nums[i])
            ans=max(ans,dp[i])
            heapq.heappush(heap,(-dp[i],i))
        return ans
