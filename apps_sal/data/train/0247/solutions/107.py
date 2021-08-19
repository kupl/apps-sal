class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        (start, window_sum, result) = (0, 0, float('inf'))
        pre_min = len(arr) * [float('inf')]
        for (i, num) in enumerate(arr):
            window_sum += num
            while window_sum > target:
                window_sum -= arr[start]
                start += 1
            if window_sum == target:
                curr_len = i - start + 1
                result = min(result, curr_len + pre_min[start - 1])
                pre_min[i] = min(curr_len, pre_min[i - 1])
            else:
                pre_min[i] = pre_min[i - 1]
        return result if result < float('inf') else -1
