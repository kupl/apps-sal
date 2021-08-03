class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        ans = 0
        for f, l in zip([L, M], [M, L]):
            max_first = first = sum(A[:f])
            ans = max(ans, first + sum(A[f:f + l]))
            for i in range(f, len(A) - l):
                first = first + A[i] - A[i - f]
                max_first = max(max_first, first)
                ans = max(ans, max_first + sum(A[i + 1:i + 1 + l]))

        return ans
