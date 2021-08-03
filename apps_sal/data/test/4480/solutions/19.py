class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        for i in range(1, len(A)):
            A[i] = A[i] + A[i - 1]

        sumTarg = A[-1] / 3

        first = False

        for i in range(len(A)):
            if A[i] == sumTarg and first == False:
                first = True
            elif (first == True and A[i] == 2 * sumTarg and i != len(A) - 1):
                return True

        return False
