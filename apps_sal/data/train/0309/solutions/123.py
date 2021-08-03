class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i, a2 in enumerate(A[1:], start=1):
            for j, a1 in enumerate(A[:i]):
                d = a2 - a1
                if (j, d) in dp:
                    dp[i, d] = dp[j, d] + 1
                else:
                    dp[i, d] = 2
        return max(dp.values())

        f = collections.defaultdict(int)
        maxlen = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                #fff[(A[i], diff)] = max(fff[(A[i], diff)], fff.get((A[j], diff), 1) + 1)
                f[(i, diff)] = max(f[(i, diff)], f.get((j, diff), 1) + 1)
                '''
                if (j, diff) not in f:
                    f[(i, diff)] = 2
                else:
                    f[(i, diff)] = max(f[(i, diff)],  f[(j, diff)] + 1)                
                '''
                maxlen = max(maxlen, f[(i, diff)])

        return maxlen
