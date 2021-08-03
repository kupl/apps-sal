class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minHeap, maxHeap = [], []
        left = maxLen = 0
        for right in range(len(nums)):
            heappush(minHeap, (nums[right], right))
            heappush(maxHeap, (-nums[right], right))

            while nums[right] - minHeap[0][0] > limit:
                left = max(left, (heappop(minHeap)[1]) + 1)
            while -maxHeap[0][0] - nums[right] > limit:
                left = max(left, (heappop(maxHeap)[1]) + 1)
            maxLen = max(maxLen, right - left + 1)
        return maxLen
