class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = [nums[0]]
        max_deque = [nums[0]]
        max_stretch = 1
        start = 0
        end = 0
        while end < len(nums) - 1:
            end += 1
            while len(min_deque) > 0 and nums[end] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[end])
            while len(max_deque) > 0 and nums[end] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[end])
            while max_deque[0] - min_deque[0] > limit:
                if min_deque[0] == nums[start]:
                    min_deque.pop(0)
                if max_deque[0] == nums[start]:
                    max_deque.pop(0)
                start += 1
            if end - start + 1 > max_stretch:
                max_stretch = end - start + 1
        return max_stretch
