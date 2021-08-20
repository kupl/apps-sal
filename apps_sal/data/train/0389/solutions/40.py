class Solution:

    def splitArraySameAverage(self, A: List[int]) -> bool:
        from fractions import Fraction
        ALen = len(A)
        s = sum(A)
        if ALen == 1:
            return False
        for i in range(ALen):
            A[i] -= Fraction(s, ALen)
        A.sort()
        leftSet = {A[0]}
        for i in range(1, ALen // 2):
            leftSet = {z + A[i] for z in leftSet} | leftSet | {A[i]}
        if 0 in leftSet:
            return True
        rightSet = {A[ALen - 1]}
        for i in range(ALen // 2, ALen - 1):
            rightSet = {z + A[i] for z in rightSet} | rightSet | {A[i]}
        if 0 in rightSet:
            return True
        leftSum = sum(A[:ALen // 2])
        rightSum = sum(A[ALen // 2:])
        return any((-left in rightSet and (left, -left) != (leftSum, rightSum) for left in leftSet))
