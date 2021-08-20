class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        M = [0 for i in range(len(arr))]
        M[0] = arr[0]
        for i in range(1, len(arr)):
            if i < k:
                M[i] = max(arr[:i + 1]) * (i + 1)
            for j in range(1, min(k + 1, i + 1)):
                M[i] = max(M[i], M[i - j] + max(arr[i - j + 1:i + 1]) * j)
        return M[-1]
