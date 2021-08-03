class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if k == 1:
            return sum(arr)

        if k == len(arr):
            max_val = max(arr)
            return max_val * len(arr)

        sums = [-1 for index in range(k)]
        maxs = [-1 for index in range(k)]
        max_sum = 0

        sums[0] = arr[0]
        maxs[0] = arr[0]

        for idx in range(1, len(arr)):
            val = arr[idx]
            max_sum = max(sums)
            for ki in range(k - 1, 0, -1):
                max_val = maxs[ki - 1]
                if not max_val < 0:
                    if val <= max_val:
                        maxs[ki] = max_val
                        sums[ki] = sums[ki - 1] + max_val
                    else:
                        maxs[ki] = val
                        sums[ki] = sums[ki - 1] - max_val * ki + val * (ki + 1)
            sums[0] = max_sum + val
            maxs[0] = val
        return max(sums)
