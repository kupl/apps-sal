class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = float('-inf')
        maxleft = float('-inf')
        for i, a in enumerate(A):
            res = max(res, maxleft + a - i)
            maxleft = max(maxleft, a + i)
        return res
