class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        p = 0
        while A[p] < 0:
            A[p] = - A[p]
            p += 1
            K -= 1
            if K == 0:
                 return sum(A)
        if K % 2 == 0:
            return sum(A)
        else:
            return sum(A) - 2 * min(A[p], A[p-1])
