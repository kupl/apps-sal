class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for item in A:
            if item < 0 and K > 1:
                A[A.index(item)] = item * (-1)
                K -= 1
            elif item > 0 and K >= 2:
                K -= 2
        else:
            A.sort()
            while K != 0:
                K -= 1
                A[0] = A[0] * (-1)
        return sum(A)
