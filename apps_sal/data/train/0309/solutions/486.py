class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = {}
        mostFreq = -1
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                diff = A[i] - A[j]
                prevVal = 1
                if (i, diff) in dp:
                    prevVal = dp[(i, diff)]
                if (j, diff) in dp:
                    dp[(i, diff)] = max(dp[(j, diff)], prevVal - 1) + 1
                else:
                    if (i, diff) not in dp:
                        dp[(i, diff)] = 1
                mostFreq = max(dp[(i, diff)], mostFreq)
        return mostFreq + 1
