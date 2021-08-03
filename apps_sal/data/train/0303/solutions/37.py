class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        l = len(arr)
        results = [0] * l
        for idx, num in enumerate(arr):
            if idx < k:
                results[idx] = max(arr[:idx + 1]) * (idx + 1)
            else:
                res = 0
                for i in range(1, k + 1):
                    start = idx - i

                    tmp = results[start] + max(arr[start + 1:idx + 1]) * i

                    res = max(res, tmp)
                results[idx] = res

        return results[-1]
