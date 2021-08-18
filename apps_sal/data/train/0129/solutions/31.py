class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        n = len(A)
        pre = A[0] + 0
        res = 0
        for i in range(1, n):
            res = res if res > pre + A[i] - i else pre + A[i] - i
            pre = pre if pre > A[i] + i else A[i] + i
        return res
