class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        i = 0
        res = 0
        for j in range(1, len(A)):
            ti = A[i] + i
            res = max(A[j] - j + ti, res)
            if A[j] + j > ti:
                i = j
        return res
