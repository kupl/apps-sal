from collections import deque


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        res = 1
        slow = 0
        fast = 0
        min_queue = deque()
        max_queue = deque()
        while fast < len(nums):
            while min_queue and nums[fast] <= nums[min_queue[-1]]:
                min_queue.pop()
            while max_queue and nums[fast] >= nums[max_queue[-1]]:
                max_queue.pop()
            min_queue.append(fast)
            max_queue.append(fast)
            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                slow += 1
                if max_queue[0] < slow:
                    max_queue.popleft()
                if min_queue[0] < slow:
                    min_queue.popleft()
            res = max(res, fast - slow + 1)
            fast += 1
        return res
