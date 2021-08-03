class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1
        while left < n - 1 and arr[left] <= arr[left + 1]:
            # non-decreasing, keep increment
            left += 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1
        num_to_remove = min(n - left - 1, right)

        # general case:
        # from the left
        for curr in range(left + 1):
            if arr[curr] <= arr[right]:
                num_to_remove = min(num_to_remove, max(0, right - curr - 1))
            else:
                # arr[curr]>arr[right]
                if right < n - 1:
                    right += 1
                else:
                    # last element
                    break
        return num_to_remove
