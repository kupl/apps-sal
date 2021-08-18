class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        dp_i = [0 for i in range(len(A))]
        dp_j = [0 for i in range(len(A))]
        dp_i[0] = A[0]
        dp_j[-1] = A[-1] - (len(A) - 1)
        for i in range(1, len(A)):
            dp_i[i] = max(A[i] + i, dp_i[i - 1])
        for j in range(len(A) - 2, -1, -1):
            dp_j[j] = max(A[j] - j, dp_j[j + 1])
        max_sum = 0

        for i in range(len(A) - 1):
            max_sum = max(max_sum, dp_i[i] + dp_j[i + 1])

        return max_sum
