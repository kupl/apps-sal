class Solution:

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        (res, leftmax, cnt) = (0, 0, 0)
        for num in A:
            res = max(res, num + leftmax - cnt)
            if num > leftmax - cnt:
                leftmax = num
                cnt = 0
            cnt += 1
        return res
