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

        i = 0
        while i + 1 < N and arr[i] <= arr[i + 1]:
            i += 1

        if i == N - 1:
            return 0

        j = N - 1
        while j - 1 >= 0 and arr[j] >= arr[j - 1]:
            j -= 1

        if j == 0:
            return N - 1

        result = min(N - (N - j), N - i - 1)

        for k in range(i + 1):
            l = lowerbound(j, len(arr), arr[k])
            result = min(result, l - (k + 1))

        return result
