class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if not A:
            return 0
        (max_sum, cur_max, min_sum, cur_min, total) = (A[0], 0, A[0], 0, 0)
        for a in A:
            cur_max = max(a + cur_max, a)
            max_sum = max(max_sum, cur_max)
            cur_min = min(a + cur_min, a)
            min_sum = min(min_sum, cur_min)
            total += a
        return max(max_sum, total - min_sum) if total > min_sum else max_sum
