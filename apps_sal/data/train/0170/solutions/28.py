class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        p = 1
        while p < len(arr) and arr[p] >= arr[p - 1]:
            p += 1
        first = p
        p = len(arr) - 1
        while p >= 1 and arr[p] >= arr[p - 1]:
            p -= 1
        second = p
        ans = min(len(arr) - first, second)
        (i, j) = (0, second)
        while i < first and j < len(arr):
            if arr[i] > arr[j]:
                ans = min(ans, j - i)
                j += 1
            else:
                i += 1
        ans = min(ans, j - i)
        return ans if ans > 0 else 0
