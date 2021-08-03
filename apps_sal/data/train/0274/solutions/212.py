class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxque = collections.deque([])
        minque = collections.deque([])
        start = end = 0
        count = 0
        while end < len(nums):
            while len(maxque) and nums[end] > nums[maxque[-1]]:
                maxque.pop()
            while len(minque) and nums[end] < nums[minque[-1]]:
                minque.pop()
            maxque.append(end)
            minque.append(end)
            if nums[maxque[0]] - nums[minque[0]] > limit:
                if maxque[0] == start:
                    maxque.popleft()
                if minque[0] == start:
                    minque.popleft()
                start += 1
                end += 1
            else:
                end += 1

        return len(nums) - start
