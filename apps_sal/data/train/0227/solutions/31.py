class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, right = 0, 0
        max_window = 0
        zero_positions = []
        num_violations = 0
        while right < len(A):
            if A[right] == 0:
                num_violations += 1
                zero_positions.append(right)
            if num_violations > K:
                left = zero_positions[0] + 1
                zero_positions.pop(0)
                num_violations -= 1
            right += 1
            max_window = max(max_window, right - left)
        return max_window
