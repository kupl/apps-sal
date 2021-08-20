class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        l = len(A)
        if L < M:
            (M, L) = (L, M)
        ans = 0
        for i in range(l - L + 1):
            tmp = sum(A[i:i + L])
            j = 0
            while j < l - M + 1:
                if i < j + M < i + L:
                    j = i + L
                else:
                    ans = max(ans, tmp + sum(A[j:j + M]))
                    j += 1
        return ans
