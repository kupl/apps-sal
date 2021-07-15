class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        seen = {}
        res = 0
        for i in range(len(A)):
            for j in range(i-1, -1, -1):
                diff = A[i] - A[j]
                if diff not in seen:
                    seen[diff] = {}
                old_val = seen[diff][i] if i in seen[diff] else 0
                if j not in seen[diff]:
                    seen[diff][i] = 2
                else:
                    seen[diff][i] = seen[diff][j] + 1
                seen[diff][i] = max(old_val, seen[diff][i])
                if seen[diff][i] > res:
                    res = seen[diff][i]
        return res
