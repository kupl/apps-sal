class Solution:

    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        longestMountain = 0
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                left = right = i
                while left > 0 and A[left - 1] < A[left]:
                    left -= 1
                while right + 1 < len(A) and A[right + 1] < A[right]:
                    right += 1
                mountainLength = right - left + 1
                longestMountain = max(longestMountain, mountainLength)
        return longestMountain
