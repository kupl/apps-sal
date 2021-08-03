class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0 - sys.maxsize for i in range(len(nums))]
        heap = []

        dp[0] = nums[0]
        heapq.heappush(heap, (0 - nums[0], 0))
        for i in range(1, len(nums)):
            while len(heap) and heap[0][1] < i - k:
                heapq.heappop(heap)
            dp[i] = max(dp[i], nums[i] + max(0, 0 - heap[0][0] if len(heap) else 0))
            heapq.heappush(heap, (0 - dp[i], i))
        return max(dp)
