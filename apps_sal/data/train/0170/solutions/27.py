class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        i = 0
        while i < len(arr) - 1 and arr[i] <= arr[i + 1]:
            i += 1
        if i == len(arr):
            return 0
        j = len(arr) - 1
        while j and arr[j - 1] <= arr[j]:
            j -= 1
        if j == -1:
            return 0

        def lowerbound(left, right, target):
            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    right = mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        N = len(arr)
        print((i, j))
        out = min(N - (N - j), N - i - 1)
        print(out)
        for k in range(i + 1):
            hi = lowerbound(j, len(arr), arr[k])
            out = min(out, hi - k - 1)
        return max(0, out)
