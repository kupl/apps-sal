class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        (left, right) = (0, len(arr) - 1)
        while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
            left += 1
        if left == len(arr) - 1:
            return 0
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        best = min(len(arr) - 1 - left, right)
        for i in range(left + 1):
            if arr[i] <= arr[right]:
                best = min(best, right - i - 1)
            elif right < len(arr) - 1:
                right += 1
            else:
                break
        return best
