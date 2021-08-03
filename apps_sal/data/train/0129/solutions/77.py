class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # we have to find A[i] + i + A[j] - j
        # we will fix max(A[i] + i) and find for diff values of A[j] - j
        if len(A) == 0:
            return 0
        maxI = A[0] + 0
        res = 0
        for j in range(1, len(A)):
            res = max(res, maxI + A[j] - j)
            maxI = max(maxI, A[j] + j)
        return res

        # for i in range(len(A)-1):
        #     for j in range(i+1,len(A)):
        #         score = max(score,A[i] + A[j] + i - j)
        # return score
