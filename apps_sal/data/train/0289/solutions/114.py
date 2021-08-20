class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        (temp, prefix_sums) = (0, [0])
        N = len(A)
        maxsum = 0
        for i in range(N):
            prefix_sums.append(temp + A[i])
            temp += A[i]
        for i in range(0, N - L + 1):
            for j in range(0, i - M + 1):
                if j < 0:
                    continue
                sum1 = prefix_sums[i + L] - prefix_sums[i]
                sum2 = prefix_sums[j + M] - prefix_sums[j]
                maxsum = max(maxsum, sum1 + sum2)
            for j in range(i + L, N - M + 1):
                if j + M - 1 >= N:
                    continue
                sum1 = prefix_sums[i + L] - prefix_sums[i]
                sum2 = prefix_sums[j + M] - prefix_sums[j]
                maxsum = max(maxsum, sum1 + sum2)
        return maxsum
