class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        k = 0
        while k + 1 < len(arr) and arr[k + 1] >= arr[k]:
            k += 1
        if k == len(arr) - 1:
            return 0
        l = len(arr) - 1
        while l > 0 and arr[l - 1] <= arr[l]:
            l -= 1
        ans = max(k + 1, len(arr) - l)
        for i in range(k + 1):
            while l < len(arr) and arr[i] > arr[l]:
                l += 1
            ans = max(ans, i + 1 + len(arr) - l)
        return len(arr) - ans
