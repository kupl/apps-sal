class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if arr == sorted(arr):
            return 0
        for head in range(len(arr) - 1):
            if arr[head] > arr[head + 1]:
                break
        if head == len(arr):
            return 0 # already sorted
        for tail in range(len(arr) - 1, 0, -1):
            if arr[tail - 1] > arr[tail]:
                break
        lo = head + 1
        hi = len(arr)
        output = float('inf')
        while lo >= 0:
            while hi - 1 >= tail and (lo == 0 or arr[lo - 1] <= arr[hi - 1]):
                hi -= 1
            output = min(output, hi - lo)
            lo -= 1
        return output
