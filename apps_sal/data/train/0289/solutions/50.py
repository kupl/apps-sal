class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        prefix_sum = [0] * (len(A) + 1)
        for i in range(len(A)):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]
        maxL = maxM = result = 0
        for i in range(M, len(prefix_sum) - L):
            maxM = max(maxM, prefix_sum[i] - prefix_sum[i - M])
            result = max(result, maxM + prefix_sum[i + L] - prefix_sum[i])
        for i in range(L, len(prefix_sum) - M):
            maxL = max(maxL, prefix_sum[i] - prefix_sum[i - L])
            result = max(result, maxL + prefix_sum[i + M] - prefix_sum[i])
        return result
