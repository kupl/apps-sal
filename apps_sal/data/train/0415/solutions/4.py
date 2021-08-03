class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        not_swap, swap = 0, 1
        for i in range(1, N):
            not_swap2 = swap2 = N
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                swap2 = swap + 1
                not_swap2 = not_swap
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                swap2 = min(swap2, not_swap + 1)
                not_swap2 = min(not_swap2, swap)
            swap, not_swap = swap2, not_swap2
        return min(swap, not_swap)
