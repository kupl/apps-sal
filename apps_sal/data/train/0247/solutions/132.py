class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        left, right = 0, 0
        valid_subarray_lengths = [0 for _ in range(len(arr))]
        cum_sum = 0
        for i in range(len(arr)):
            cum_sum += arr[i]
            right = i
            while cum_sum > target:
                cum_sum -= arr[left]
                left += 1
            if cum_sum == target:
                valid_subarray_lengths[i] = right - left + 1
        prefix_min_lengths = [None for _ in range(len(valid_subarray_lengths))]
        prefix_min = float('inf')
        for i in range(len(valid_subarray_lengths)):
            prefix_min = min(prefix_min, valid_subarray_lengths[i] if valid_subarray_lengths[i] else float('inf'))
            prefix_min_lengths[i] = prefix_min
        res = float('inf')
        for i in range(len(valid_subarray_lengths)):
            if valid_subarray_lengths[i] != 0 and i - valid_subarray_lengths[i] >= 0 and prefix_min_lengths[i - valid_subarray_lengths[i]] > 0:
                res = min(res, valid_subarray_lengths[i] + prefix_min_lengths[i - valid_subarray_lengths[i]])
        return res if res != float('inf') else -1
