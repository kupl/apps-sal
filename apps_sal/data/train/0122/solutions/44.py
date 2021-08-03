class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        su = sum(A[:k])
        res = su
        for i in range(k):
            su -= A[k - i - 1]
            su += A[len(A) - i - 1]
            res = max(res, su)
        return res
