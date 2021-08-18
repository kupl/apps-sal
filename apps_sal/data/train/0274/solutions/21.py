from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        minDeque = deque()
        maxDeque = deque()
        left = 0
        right = 0
        result = 0
        while right < len(nums):
            while minDeque and nums[right] < nums[minDeque[-1]]:
                minDeque.pop()
            while maxDeque and nums[right] > nums[maxDeque[-1]]:
                maxDeque.pop()
            minDeque.append(right)
            maxDeque.append(right)
            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                while maxDeque[0] <= left:
                    maxDeque.popleft()
                while minDeque[0] <= left:
                    minDeque.popleft()
                left += 1
            result = max(result, right - left + 1)
            right += 1
        return result
