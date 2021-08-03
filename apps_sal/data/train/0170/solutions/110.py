class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)

        left_idx = 0
        while left_idx < N - 1 and arr[left_idx] <= arr[left_idx + 1]:
            left_idx += 1

        if left_idx == N - 1:
            return 0

        right_idx = N - 1
        while right_idx > 1 and arr[right_idx] >= arr[right_idx - 1]:
            right_idx -= 1

        r = min(N - 1 - left_idx, right_idx)

        i = 0
        j = right_idx
        while i <= left_idx and j <= N - 1:
            if arr[j] >= arr[i]:
                r = min(r, j - i - 1)
                i += 1
            else:
                j += 1
        return r
