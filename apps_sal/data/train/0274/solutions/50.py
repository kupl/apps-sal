from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQue = deque()
        maxQue = deque()
        start, end = 0, 0
        longest = 1
        while end < len(nums):
            current = nums[end]
            while minQue and nums[minQue[-1]] >= current:
                minQue.pop()
            minQue.append(end)
            while maxQue and nums[maxQue[-1]] <= current:
                maxQue.pop()
            maxQue.append(end)
            if nums[maxQue[0]] - nums[minQue[0]] > limit:
                start += 1
                while maxQue and start > maxQue[0]:
                    maxQue.popleft()
                while minQue and start > minQue[0]:
                    minQue.popleft()
            else:
                longest = max(longest, end - start + 1)
                end += 1
        return longest
