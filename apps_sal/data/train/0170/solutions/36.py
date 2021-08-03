class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if arr == None or len(arr) <= 1:
            return 0
        left, right = 0, len(arr) - 1
        while left + 1 < len(arr) and arr[left] <= arr[left + 1]:
            left += 1
        if left == len(arr) - 1:
            return 0
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        result = min(len(arr) - left - 1, right)
        if arr[left] <= arr[right]:
            result = min(result, right - left - 1)
        for i in range(left + 1):
            if arr[i] <= arr[right]:
                result = min(result, right - i - 1)
            elif right < len(arr) - 1:
                right += 1
        return result
