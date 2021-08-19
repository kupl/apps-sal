class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        temp, prefix_sums = 0, [0]
        N = len(A)
        maxsum = 0

        # define prefix_sums[i] as: A[0] + A[1] + ... + A[i-1]
        for i in range(N):
            prefix_sums.append(temp + A[i])
            temp += A[i]
        # the last subarray = A[i] + A[i+1] +  ... + A[N-1], so maximum i = N - L
        for i in range(0, N - L + 1):
            for j in range(0, i - M + 1):
                # print(\"i=\",i,\"; j=\",j)
                if j < 0:
                    continue
                sum1 = prefix_sums[i + L] - prefix_sums[i]
                sum2 = prefix_sums[j + M] - prefix_sums[j]
                maxsum = max(maxsum, sum1 + sum2)

            for j in range(i + L, N - M + 1):
                # print(\"i=\",i,\"; j=\",j)
                if j + M - 1 >= N:
                    continue
                sum1 = prefix_sums[i + L] - prefix_sums[i]
                sum2 = prefix_sums[j + M] - prefix_sums[j]
                maxsum = max(maxsum, sum1 + sum2)

        return maxsum
