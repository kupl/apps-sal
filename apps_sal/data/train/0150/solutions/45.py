class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        min_right = min(A)
        max_left = 0

        min_from_right = []
        current_min_right = A[-1]
        for i in range(len(A) - 1, -1, -1):
            current_min_right = min(A[i], current_min_right)
            min_from_right.insert(0, current_min_right)

        for i in range(len(A)):
            current = A[i]
            max_left = max(max_left, current)
            min_right = min_from_right[i + 1] if i < len(A) else 0
            if max_left <= min_right:
                return i + 1
