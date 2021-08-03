class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:

        cumSum = [0] * (len(A) + 1)

        for i, a in enumerate(A):
            cumSum[i + 1] = cumSum[i] + a

        max_sum = 0
        for i in range(len(A) - L + 1):
            sum_sub1 = 0
            sum_sub1 = cumSum[i + L] - cumSum[i]
            if i >= M:
                for j in range(i - M + 1):
                    sum_sub2 = 0
                    sum_sub2 = cumSum[j + M] - cumSum[j]
                    sum_sub2 = sum_sub1 + sum_sub2
                    max_sum = max(max_sum, sum_sub2)
            if i + L <= len(A) - M:
                for j in range(i + L, len(A) - M + 1):
                    sum_sub2 = 0
                    sum_sub2 = cumSum[j + M] - cumSum[j]
                    sum_sub2 = sum_sub1 + sum_sub2
                    max_sum = max(max_sum, sum_sub2)

        return max_sum
