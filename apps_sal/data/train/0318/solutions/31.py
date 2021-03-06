class Solution:

    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3

        def get_maxsubseq(pieces):
            m = len(pieces)
            dp = {}
            for i in range(1, n + 1):
                tdp = {}
                for j in range(m):
                    tdp[j] = max(dp.get(j - 2, 0) + pieces[j], tdp.get(j - 1, 0))
                dp = tdp
            return dp[m - 1]
        return max(get_maxsubseq(slices[1:]), get_maxsubseq(slices[:-1]))
