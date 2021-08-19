class Solution:

    def shipWithinDays(self, arr: List[int], D: int) -> int:

        def count(arr, x):
            res = i = 0
            while i < len(arr):
                z = 0
                while i < len(arr) and z + arr[i] <= x:
                    z += arr[i]
                    i += 1
                res += 1
            return res
        end = start = 0
        for i in arr:
            end += i
            start = max(start, i)
        while start <= end:
            mid = start + (end - start) // 2
            if count(arr, mid) > D:
                start = mid + 1
            else:
                out = mid
                end = mid - 1
        return out
