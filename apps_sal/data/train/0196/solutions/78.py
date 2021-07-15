class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def find_max_sum(A):
            curr_sum = 0
            max_sum = -math.inf
            for num in A:
                if curr_sum > 0:
                    curr_sum += num
                else:
                    curr_sum = num
                max_sum = max(max_sum, curr_sum)
            return max_sum
        max_sum = find_max_sum(A)
        min_sum_1 = -find_max_sum(-num for num in A[1:])
        min_sum_2 = -find_max_sum(-num for num in A[:-1])
        return max(sum(A) - min(min_sum_1, min_sum_2), max_sum)
