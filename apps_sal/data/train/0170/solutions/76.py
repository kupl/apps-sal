class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        (start, end) = (0, 0)
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1] or (start and arr[i] < arr[start - 1]):
                if not start:
                    start = i
                end = i
        if start > 0:
            if arr[end] >= arr[start - 1]:
                end -= 1
            curr_opt = end - start + 1
        else:
            curr_opt = end - start
        for i in range(start):
            start -= 1
            while (end == len(arr) - 1 or arr[end] <= arr[end + 1]) and (start and arr[end] >= arr[start - 1] or not start):
                end -= 1
            curr_opt = min(curr_opt, end - start + 1)
        return curr_opt
