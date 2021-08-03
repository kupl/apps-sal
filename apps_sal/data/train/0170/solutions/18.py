class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 1, 1

        i = 1
        while i < n and arr[i] >= arr[i - 1]:
            left += 1
            i += 1

        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            right += 1
            i -= 1

        l1, l2 = right, left

        i = n - right
        while i < n and arr[i] < arr[left - 1]:
            i += 1
            l1 -= 1

        i = left - 1
        while i >= 0 and arr[i] > arr[n - right]:
            i -= 1
            l2 -= 1

        return max(min(n - left - l1, n - right - l2), 0)
