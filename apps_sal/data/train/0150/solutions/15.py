class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        left = [0 for i in range(len(A))]
        left[0] = A[0]
        for i in range(1, len(A)):
            left[i] = max(left[i - 1], A[i])
        right = [0 for i in range(len(A))]
        right[-1] = A[-1]
        for i in reversed(range(len(A) - 1)):
            right[i] = min(right[i + 1], A[i])
        for i in range(len(A) - 1):
            if left[i] <= right[i + 1]:
                return i + 1
