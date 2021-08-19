class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        (maxAB, currA, currB) = (1, 1, 1)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                currA = currB + 1
                currB = 1
            elif A[i] < A[i - 1]:
                currB = currA + 1
                currA = 1
            else:
                (currA, currB) = (1, 1)
            maxAB = max(maxAB, currA, currB)
        return maxAB
