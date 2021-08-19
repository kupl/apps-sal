class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [n for n in nums]
        heap = [(-nums[0], 0)]
        for j in range(1, len(nums)):
            while heap[0][1] < j - k:
                heapq.heappop(heap)
            dp[j] = max(dp[j], -heap[0][0] + nums[j])
            heapq.heappush(heap, (-dp[j], j))
        return max(dp)
