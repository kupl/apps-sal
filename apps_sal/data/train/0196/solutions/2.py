class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if not A:
            return 0
        max_A = max(A)
        if max_A <= 0:
            return max_A
        max_sum = 0
        cur_sum = 0
        for i in range(len(A)):
            cur_sum = max(cur_sum, 0) + A[i]
            max_sum = max(max_sum, cur_sum)
        if len(A) <= 2:
            return max_sum
        right_sum = A[-1]
        right_max = [A[-1]]
        for i in A[len(A) - 2::-1]:
            right_sum += i
            right_max.append(max(right_max[-1], right_sum))
        right_max = right_max[::-1]
        left_max = A[0]
        left_sum = A[0]
        for i in range(1, len(A) - 1):
            left_sum += A[i]
            left_max = max(left_max, left_sum)
            max_sum = max(max_sum, left_max + right_max[i + 1])
        return max_sum
