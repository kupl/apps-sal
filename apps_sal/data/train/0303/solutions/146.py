class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        result = [0] * len(arr)
        result[0] = arr[0]
        max_val = result[0]
        for i in range(1, k):
            max_val = max(max_val, arr[i])
            result[i] = max_val * (i + 1)
        for i in range(k, len(arr)):
            max_val = arr[i]
            for j in range(1, k + 1):
                max_val = max(max_val, arr[i - j + 1])
                result[i] = max(result[i], result[i - j] + max_val * j)
        return result[-1]
