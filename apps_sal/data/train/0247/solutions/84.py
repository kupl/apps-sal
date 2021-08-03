class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        if not arr:
            return 0

        min_at_curr = [float('inf')] * len(arr)
        start = end = 0
        currSum = 0
        minSum = float('inf')

        while end < len(arr):
            currSum += arr[end]

            while start <= end and currSum > target:
                currSum -= arr[start]
                start += 1

            if currSum == target:
                minSum = min(minSum, min_at_curr[start - 1] + (end - start) + 1)
                min_at_curr[end] = min(min_at_curr[end - 1], end - start + 1)

            else:
                min_at_curr[end] = min_at_curr[end - 1]

            end += 1

        return minSum if minSum != float('inf') else -1
