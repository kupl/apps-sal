class Solution:

    def minDifference(self, A: List[int]) -> int:
        if len(A) <= 4:
            return 0
        A = sorted(A)
        res = math.inf
        for i in range(4):
            res = min(res, A[len(A) - i - 1] - A[3 - i])
        return res
