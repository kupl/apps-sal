class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        new_array = list()
        current_segment = 0
        for num in nums:
            if num == 0:
                if current_segment > 0:
                    new_array.append(current_segment)
                    current_segment = 0
                new_array.append(0)
            else:
                current_segment += 1
        if current_segment > 0:
            new_array.append(current_segment)
        max_length = 0
        for idx in range(len(new_array)):
            max_length = max(max_length, new_array[idx])
            if idx > 0 and idx < len(new_array) - 1 and (new_array[idx] == 0):
                if new_array[idx - 1] > 0 and new_array[idx + 1] > 0:
                    max_length = max(max_length, new_array[idx - 1] + new_array[idx + 1])
        if max_length == len(nums):
            return max_length - 1
        else:
            return max_length
