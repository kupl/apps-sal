class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        left = [0] * len(A)
        left[0] = A[0]
        for i in range(1, len(A)):
            left[i] = max(A[i], left[i - 1])
        right = [0] * len(A)
        right[-1] = A[-1]
        for i in range(len(A) - 2, -1, -1):
            right[i] = min(A[i], right[i + 1])
        print((*left))
        print((*right))
        for i in range(1, len(A)):
            if right[i] >= left[i - 1]:
                return i
