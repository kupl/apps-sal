class Solution:

    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        max_eh = arr[0]
        min_eh = arr[0]
        max_sf = arr[0]
        min_sf = arr[0]
        total = sum(arr)
        for i in range(1, len(arr)):
            max_eh = max(max_eh + arr[i], arr[i])
            max_sf = max(max_eh, max_sf)
            min_eh = min(min_eh + arr[i], arr[i])
            min_sf = min(min_eh, min_sf)
        if min_sf == total:
            return max_sf
        else:
            return max(max_sf, total - min_sf)
