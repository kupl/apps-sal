class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_subarray = float('-inf')
        cur_max_subarray = 0
        min_subarray = float('inf')
        cur_min_subarray = 0
        total = 0
        max_value = float('-inf')
        for num in A:
            cur_max_subarray += num
            if cur_max_subarray < 0:
                cur_max_subarray = 0
            else:
                max_subarray = max(max_subarray, cur_max_subarray)
            cur_min_subarray += num
            if cur_min_subarray > 0:
                cur_min_subarray = 0
            else:
                min_subarray = min(min_subarray, cur_min_subarray)
            total += num
            max_value = max(max_value, num)
        if max_value <= 0:
            return max_value
        return max(max_subarray, total - min_subarray)
