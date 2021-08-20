class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        result = 0
        min_deque = []
        max_deque = []
        start = 0
        for (index, value) in enumerate(nums):
            while len(min_deque) and value < min_deque[-1]:
                min_deque.pop()
            while len(max_deque) and value > max_deque[-1]:
                max_deque.pop()
            min_deque.append(value)
            max_deque.append(value)
            while max_deque[0] - min_deque[0] > limit:
                if nums[start] == min_deque[0]:
                    min_deque.pop(0)
                if nums[start] == max_deque[0]:
                    max_deque.pop(0)
                start += 1
            result = max(result, index - start + 1)
        return result
