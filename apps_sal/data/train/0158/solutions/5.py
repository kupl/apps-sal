class Solution:

    @lru_cache(maxsize=None)
    def kSimilarity(self, A: str, B: str) -> int:
        if not A and (not B):
            return 0
        if A[0] == B[0]:
            return self.kSimilarity(A[1:], B[1:])
        ans = float('inf')
        for (i, c) in enumerate(B):
            if c == A[0]:
                ans = min(ans, 1 + self.kSimilarity(A[1:], B[1:i] + B[0] + B[i + 1:]))
        return ans
