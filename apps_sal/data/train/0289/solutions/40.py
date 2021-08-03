from typing import List


class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        def findMaxSum(A, L, M):
            max_sum = 0

            for i in range(len(A) - L):
                L_slice = A[i: L + i]
                L_sum = sum(L_slice)

                for j in range(L + i, len(A) - M + 1):
                    M_slice = A[j: M + j]
                    M_sum = sum(M_slice)

                    max_sum = max(max_sum, L_sum + M_sum)
            return max_sum

        forward_sum = findMaxSum(A, L, M)
        A.reverse()
        backward_sum = findMaxSum(A, L, M)

        return max(forward_sum, backward_sum)
