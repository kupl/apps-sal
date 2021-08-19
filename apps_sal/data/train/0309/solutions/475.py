class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) <= 2:
            return len(A)
        seen = {}
        ans = 0
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                seen[j, A[j] - A[i]] = seen.get((i, A[j] - A[i]), 0) + 1
                ans = max(ans, seen[j, A[j] - A[i]])
        return ans + 1
