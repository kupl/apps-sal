class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        prefix = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            prefix[i] = prefix[i - 1] + A[i - 1]

        def get_subsum(i, j):
            return prefix[j + 1] - prefix[i]
        result = 0
        for i in range(len(A) - L - M + 1):
            sub1 = get_subsum(i, i + L - 1)
            for j in range(i + L, len(A) - M + 1):
                sub2 = get_subsum(j, j + M - 1)
                result = max(result, sub1 + sub2)
        for i in range(len(A) - L - M + 1):
            sub1 = get_subsum(i, i + M - 1)
            for j in range(i + M, len(A) - L + 1):
                sub2 = get_subsum(j, j + L - 1)
                result = max(result, sub1 + sub2)
        return result
