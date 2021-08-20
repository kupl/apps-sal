class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr = [float('inf') for _ in range(n + 1)]
        arr[0] = 0
        i = 0
        while i < len(arr):
            left = max(0, i - ranges[i])
            right = min(len(arr) - 1, i + ranges[i])
            j = left + 1
            while j <= right:
                arr[j] = min(arr[j], 1 + arr[left])
                j += 1
            i += 1
        if arr[-1] == float('inf'):
            return -1
        return arr[-1]
