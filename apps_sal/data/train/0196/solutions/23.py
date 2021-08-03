import sys


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(A, n):
            maxG = 0
            curr_max = 0
            for i in range(n):
                curr_max += A[i]
                curr_max = max(0, curr_max)
                maxG = max(maxG, curr_max)

            return maxG

        flag = None
        for i in A:
            if i > 0:
                flag = 1
                break
        if not flag:
            return max(A)

        n = len(A)
        noWrap = kadane(A, n)
        total = 0
        for i in range(n):
            total += A[i]
            A[i] *= -1
        minTotal = kadane(A, n)
        maxG = total + minTotal
        return max(noWrap, maxG)
