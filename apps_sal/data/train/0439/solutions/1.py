class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return 1
        start = 0
        prev_trend = None
        max_window_length = 0
        for end in range(1, n):
            max_window_length = max(max_window_length, end - start)
            if A[end] > A[end - 1]:
                current_trend = 'inc'
            elif A[end] < A[end - 1]:
                current_trend = 'dec'
            else:
                current_trend = None
            if current_trend and prev_trend == current_trend:
                start = end - 1
            elif current_trend is None:
                start = end
            prev_trend = current_trend
        max_window_length = max(max_window_length, end - start + 1)
        return max_window_length
