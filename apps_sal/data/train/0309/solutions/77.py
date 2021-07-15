class Solution:
    def longestArithSeqLength(self, A):
        dp = dict()
        for endi, endv in enumerate(A[1:], start = 1):
            for starti, startv in enumerate(A[:endi]):
                diff = endv - startv
                if (starti, diff) in dp:
                    dp[(endi, diff)] = dp[(starti, diff)] + 1
                else:
                    dp[(endi, diff)] = 2
        return max(dp.values())
        


