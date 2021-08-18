class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        res = 0
        left, right = 0, 0
        minimum, maximum = [], []
        while right < n:
            heapq.heappush(minimum, (nums[right], right))
            heapq.heappush(maximum, (-nums[right], right))
            right += 1
            while -maximum[0][0] - minimum[0][0] > limit:
                while minimum and minimum[0][1] <= left:
                    heapq.heappop(minimum)
                while maximum and maximum[0][1] <= left:
                    heapq.heappop(maximum)
                left += 1
            res = max(res, right - left)
        return res
