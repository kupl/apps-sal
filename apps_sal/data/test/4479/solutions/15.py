class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        while K > 0:
            t = A.index(min(A))
            if A[t] < 0:
                A[t] = abs(A[t])
                K -= 1
                continue
            if A[t] == 0:
                K = 0
                continue
            if A[t] > 0:
                if K % 2 == 0:
                    K = 0
                    continue
                else:
                    A[t] = -A[t]
                    K = 0
                    continue
        return sum(A)
