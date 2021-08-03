class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        sliding_window_counter = collections.Counter()
        result = 0

        for end in range(len(nums)):
            sliding_window_counter[nums[end]] += 1

            while sliding_window_counter[0] > 1:
                sliding_window_counter[nums[start]] -= 1
                start += 1
            result = max(result, end - start)

        return result
