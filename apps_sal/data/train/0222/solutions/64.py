class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0

        S = set(A)
        ans = 0
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                l = 2
                x, y = A[j], A[i] + A[j]
                while y in S:
                    l += 1
                    x, y = y, x + y
                ans = max(ans, l)

        return ans if ans >= 3 else 0
