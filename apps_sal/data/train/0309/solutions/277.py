class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) == 1:
            return 1
        if len(A) == 2:
            return 2
        N = len(A)
        ans = 2
        seen = {}
        for i in range(N):
            for j in range(i + 1, N):
                diff = A[j] - A[i]
                if (i, diff) in seen:
                    ans = max(ans, seen[i, diff] + 1)
                    seen[j, diff] = seen[i, diff] + 1
                else:
                    seen[j, diff] = 2
        return ans
