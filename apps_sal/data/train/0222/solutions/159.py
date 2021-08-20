class Solution:

    def lenLongestFibSubseq(self, lst: List[int]) -> int:
        m = 0
        dp = {}
        for i in range(len(lst)):
            for j in range(i):
                j1 = (j, lst[i])
                i1 = (i, lst[i] + lst[j])
                if j1 in dp:
                    dp[i1] = 1 + dp[j1]
                else:
                    dp[i1] = 2
                m = max(m, dp[i1])
        if m < 3:
            return 0
        return m
