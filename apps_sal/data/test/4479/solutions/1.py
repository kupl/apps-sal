class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        while(i < len(A) and A[i] < 0 and i < K):
            A[i] = -A[i]
            i += 1

        return sum(A) - (K - i) % 2 * min(A) * 2
