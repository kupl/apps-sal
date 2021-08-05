class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        def findMaxSum(A: List[int], L: int, M: int) -> int:
            max_num = 0
            for i in range(len(A) - L):
                L_slice = A[i:L + i]
                L_sum = sum(L_slice)
                for j in range(L + i, len(A) - M + 1):
                    M_slice = A[j:M + j]
                    M_sum = sum(M_slice)
                    max_num = max(L_sum + M_sum, max_num)
            return max_num

        forwards_sum = findMaxSum(A, L, M)
        A.reverse()
        backwards_sum = findMaxSum(A, L, M)
        return max(forwards_sum, backwards_sum)
