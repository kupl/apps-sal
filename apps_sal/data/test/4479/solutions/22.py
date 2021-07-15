class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for i in range(K):
            A[0] = -1 * A[0]
            if A[0] > A[1]:
                A.append(A.pop(0))
        return sum(A)        
