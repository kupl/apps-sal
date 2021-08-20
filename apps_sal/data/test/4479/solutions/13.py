class Solution:

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        B = sorted(A)
        for i in range(K):
            B[0] = -B[0]
            B = sorted(B)
        return sum(B)
