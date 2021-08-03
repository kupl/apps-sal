class Solution:
    def longestMountain(self, A: List[int]) -> int:
        # Write your code here.
        longest, i = 0, 1
        while i < len(A) - 1:
            is_peak = A[i - 1] < A[i] and A[i] > A[i + 1]
            # Check if i is peak
            if is_peak:
                left = i - 2
                # Move left pointer left while in bounds and greater
                while left >= 0 and A[left] < A[left + 1]:
                    left -= 1
                right = i + 2
                # Move right pointer right while in bounds and greater
                while right < len(A) and A[right] < A[right - 1]:
                    right += 1
                # Current peak
                longest = max(longest, right - left - 1)
                # Increment i
                i = right
            # If i is not peak, increment and continue.
            else:
                i += 1
                continue
        return longest
