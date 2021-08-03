class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        two_sum = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                two_sum[(A[i], A[j])] = 2

        result = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (A[j] - A[i], A[i]) in two_sum:
                    two_sum[(A[i], A[j])] = max(two_sum[(A[i], A[j])], two_sum[(A[j] - A[i], A[i])] + 1)
                    result = max(result, two_sum[(A[i], A[j])])
        return result
