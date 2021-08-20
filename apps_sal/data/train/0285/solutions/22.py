class Solution:

    def smallestRangeII(self, arr: List[int], k: int) -> int:
        arr.sort()
        best = arr[-1] - arr[0]
        for i in range(1, len(arr)):
            current_max = max(arr[-1] - k, arr[i - 1] + k)
            current_min = min(arr[0] + k, arr[i] - k)
            best = min(best, current_max - current_min)
        return best
