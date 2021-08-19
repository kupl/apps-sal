class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        if L + M == n:
            return sum(A)
        cumsum = [0] * (n + 1)
        for i in range(n):
            cumsum[i + 1] = cumsum[i] + A[i]

        def good_combo(i, j):
            return i + L - 1 < j or j + M - 1 < i
        res = -float('inf')
        for i in range(n - L + 1):
            for j in range(n - M + 1):
                if good_combo(i, j):
                    res = max(res, cumsum[i + L] - cumsum[i] + cumsum[j + M] - cumsum[j])
        return res
