class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_sum = min_sum = A[0]
        curr_max = curr_min = tot = 0
        for a in A:
            curr_max = max(curr_max + a, a)
            curr_min = min(curr_min + a, a)
            max_sum = max(curr_max, max_sum)
            min_sum = min(curr_min, min_sum)
            tot += a
        return max(max_sum, tot - min_sum) if max_sum > 0 else max_sum

