class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        S = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            S[i] += S[i - 1] + A[i - 1]
        (lmax, rmax) = (0, 0)
        for j in range(L, len(S) - M):
            lmax = max(lmax, S[j] - S[j - L])
            rmax = max(rmax, S[j + M] - S[j] + lmax)
        (lmax2, rmax2) = (0, 0)
        for j in range(M, len(S) - L):
            lmax2 = max(lmax2, S[j] - S[j - M])
            rmax2 = max(rmax2, S[j + L] - S[j] + lmax2)
        return max(rmax, rmax2)
