class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        left = 0
        res = 0
        max_pre = 0
        curr_res = 0
        for right in range(1, len(A)):
            max_pre = max(max_pre, A[right-1] + (right-1))
            curr_res = max_pre + A[right] - right
            res = max(res, curr_res)
        return res
