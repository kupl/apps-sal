class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
        m = n - 1
        left_max = [0] * m
        left_max[0] = A[0]
        right_min = [0] * m
        right_min[-1] = A[-1]
        for i in range(1, n - 1):
            left_max[i] = max(left_max[i - 1], A[i])
        for i in reversed(range(1, m)):
            right_min[i - 1] = min(right_min[i], A[i])
        for i in range(m):
            if left_max[i] <= right_min[i]:
                return i + 1
