class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = 0
        j = 0
        bestSize = 0
        maxVals = []
        minVals = []
        import heapq
        while j < len(nums):
            heappush(maxVals, (-nums[j], j))
            heappush(minVals, (nums[j], j))
            if -maxVals[0][0] - minVals[0][0] > limit:
                i = min(minVals[0][1], maxVals[0][1]) + 1
                while minVals[0][1] < i:
                    heappop(minVals)
                while maxVals[0][1] < i:
                    heappop(maxVals)
            bestSize = max(bestSize, j - i + 1)
            j += 1
        return bestSize
