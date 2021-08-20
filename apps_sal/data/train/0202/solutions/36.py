class Solution:

    def longestMountain(self, A: List[int]) -> int:
        (longest, i) = (0, 1)
        while i < len(A) - 1:
            is_peak = A[i - 1] < A[i] and A[i] > A[i + 1]
            if is_peak:
                left = i - 2
                while left >= 0 and A[left] < A[left + 1]:
                    left -= 1
                right = i + 2
                while right < len(A) and A[right] < A[right - 1]:
                    right += 1
                longest = max(longest, right - left - 1)
                i = right
            else:
                i += 1
                continue
        return longest
