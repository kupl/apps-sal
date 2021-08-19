class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        lo = 0
        hi = len(A)
        A = [0] + [1 - x for x in A]
        n = len(A)
        for i in range(1, n):
            A[i] += A[i - 1]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if min((A[i] - A[i - mid] for i in range(mid, len(A)))) <= K:
                lo = mid
            else:
                hi = mid - 1
        return lo
