class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        maxa = [x + i for (i, x) in enumerate(A)]
        for i in range(1, len(maxa)):
            maxa[i] = max(maxa[i], maxa[i - 1])
        res = float('-inf')
        for j in range(1, len(A)):
            res = max(res, A[j] - j + maxa[j - 1])
        return res
