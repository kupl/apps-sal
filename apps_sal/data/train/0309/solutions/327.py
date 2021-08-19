class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        res = 0
        cache = dict()
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                if (i, diff) not in cache:
                    cache[j, diff] = 2
                else:
                    cache[j, diff] = 1 + cache[i, diff]
        return max(cache.values())


'\ndp[i][d] = longest subsequence ending at i with difference d\n\ndp[j][d] = 1 + max(\n    dp[j][A[j] - A[i]]\n) for j < i\n\n\n'
