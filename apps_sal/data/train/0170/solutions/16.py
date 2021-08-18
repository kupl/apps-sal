class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1
        num_to_remove = min(n - left - 1, right)

        for curr in range(left + 1):
            if arr[curr] <= arr[right]:
                num_to_remove = min(num_to_remove, max(0, right - curr - 1))
            else:
                if right < n - 1:
                    right += 1
                else:
                    break
        return num_to_remove
