class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:

        #         ALen = len(A)
        #         visited = set()

        #         def checkNum(i0, bN, bSum, aN, aSum):
        #             if i0 == ALen:
        #                 if aN != 0 and bN != 0 and bSum*aN == aSum*bN:
        #                     return True
        #                 return False
        #             if (i0, bN, bSum) in visited:
        #                 return False
        #             visited.add((i0, bN, bSum))
        #             subAns = checkNum(i0+1, bN+1, bSum+A[i0], aN, aSum) or checkNum(i0+1, bN, bSum, aN +1, aSum + A[i0])
        #             return subAns

        #         return checkNum(0, 0, 0, 0, 0)
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

        return any(-left in rightSet and (left, -left) != (leftSum, rightSum) for left in leftSet)
