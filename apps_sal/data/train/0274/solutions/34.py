class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maximums = [(-nums[0], 0)]
        minimums = [(nums[0], 0)]
        left = 0 if len(nums) > 1 else 1
        right = 1
        while right < len(nums):
            heapq.heappush(maximums, (-nums[right], right))
            heapq.heappush(minimums, (nums[right], right))
            right += 1
            while maximums[0][1] < left:
                heapq.heappop(maximums)
            while minimums[0][1] < left:
                heapq.heappop(minimums)
            while -maximums[0][0] - minimums[0][0] <= limit and right < len(nums):
                heapq.heappush(maximums, (-nums[right], right))
                heapq.heappush(minimums, (nums[right], right))
                right += 1
            left += 1
        if -maximums[0][0] - minimums[0][0] <= limit:
            return right - left + 1
        else:
            return right - left
