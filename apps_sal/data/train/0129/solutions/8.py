class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        sA = sorted(enumerate(A), key=lambda x: x[1], reverse=True)
        L = len(A)
        maxScore = -L
        theDis = -1
        for i in range(L - 1):
            if sA[i][1] + sA[i + 1][1] <= maxScore + 1:
                break
            for j in range(i + 1, L):
                curScore = sA[i][1] + sA[j][1]
                if curScore <= maxScore + 1:
                    break
                curDis = abs(sA[i][0] - sA[j][0])
                curScore -= curDis
                if curScore > maxScore:
                    maxScore = curScore
                    theDis = curDis
        return maxScore
