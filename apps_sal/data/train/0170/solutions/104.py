class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

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

        # find the longest ascending array on the left side
        i = 0
        while i + 1 < N and arr[i] <= arr[i + 1]:
            i += 1

        if i == N - 1:
            # it is already in ascending order
            return 0

        # find the longest ascending array on the right side
        j = N - 1
        while j - 1 >= 0 and arr[j] >= arr[j - 1]:
            j -= 1

        if j == 0:
            # the entire array is in decending order
            return N - 1

        # keep ascending array on right side or left side
        result = min(N - (N - j), N - i - 1)

        # find the shortest unordered subarray in the middle
        for k in range(i + 1):
            l = lowerbound(j, len(arr), arr[k])
            result = min(result, l - (k + 1))

        return result
