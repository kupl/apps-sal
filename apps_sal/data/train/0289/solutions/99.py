class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        l = len(A)
        presum = [0] * (l + 1)
        for i in range(l):
            presum[i + 1] = presum[i] + A[i]
        if L < M:
            (M, L) = (L, M)
        ans = 0
        for i in range(l - L + 1):
            tmp = presum[i + L] - presum[i]
            j = 0
            while j < l - M + 1:
                if i < j + M < i + L:
                    j = i + L
                else:
                    ans = max(ans, tmp + presum[j + M] - presum[j])
                    j += 1
        return ans
