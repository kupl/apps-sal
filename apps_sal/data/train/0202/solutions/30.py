class Solution:

    def longestMountain(self, A: List[int]) -> int:
        is_peak = False
        index = 1
        longest = 0
        while index < len(A) - 1:
            if A[index] > A[index - 1] and A[index] > A[index + 1]:
                is_peak = True
            if not is_peak:
                index += 1
                continue
            left = index - 1
            while left - 1 >= 0 and A[left] > A[left - 1]:
                left -= 1
            right = index + 1
            while right + 1 < len(A) and A[right] > A[right + 1]:
                right += 1
            longest = max(longest, right - left + 1)
            index = right
            is_peak = False
        return longest
