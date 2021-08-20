class Solution:

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        res = 0
        A.sort()
        i = 0
        while i < len(A) and i < K and (A[i] < 0):
            A[i] = -A[i]
            i += 1
        return sum(A) - (K - i) % 2 * 2 * min(A[i - 1:i] + A[i:i + 1])
