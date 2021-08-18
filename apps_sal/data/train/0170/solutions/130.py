class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        start_f, end_f = 0, 0
        while end_f + 1 < len(arr):
            if arr[end_f + 1] >= arr[end_f]:
                end_f += 1
            else:
                break
        if end_f == len(arr) - 1:
            return 0
        start_b, end_b = len(arr) - 1, len(arr) - 1
        if arr[-1] < arr[end_f]:
            start_b = len(arr)
        else:
            while start_b - 1 >= 0 and arr[start_b - 1] >= arr[end_f]:
                if arr[start_b - 1] <= arr[start_b]:
                    start_b -= 1
                else:
                    break
        print((start_f, end_f, start_b, end_b))
        start, end = end_f + 1, start_b - 1
        ans = end - start + 1
        while start >= 0:
            start -= 1
            while start == 0 or arr[end] >= arr[start - 1]:
                if end == len(arr) - 1 or arr[end] <= arr[end + 1]:
                    end -= 1
                    ans = min(ans, end - start + 1)
                else:
                    break
        return ans
