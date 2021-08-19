class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if A == None or len(A) == 0:
            return 0
        (max_sum, min_sum, total) = (-100000000, 1000000000, 0)
        (curr_max_sum, curr_min_sum) = (0, 0)
        for i in A:
            curr_max_sum += i
            max_sum = max(curr_max_sum, max_sum)
            curr_max_sum = max(curr_max_sum, 0)
            curr_min_sum += i
            min_sum = min(curr_min_sum, min_sum)
            curr_min_sum = min(curr_min_sum, 0)
            total += i
        return max_sum if max_sum < 0 else max(max_sum, total - min_sum)
