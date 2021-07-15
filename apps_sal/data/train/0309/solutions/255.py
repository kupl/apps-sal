class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)

        dp = collections.defaultdict(lambda: 1)
        for i in range(n):
            for j in range(i+1, n):
                dp[(j, A[j]-A[i])] = dp[(i, A[j]-A[i])] + 1
        return max(dp.values())
        

