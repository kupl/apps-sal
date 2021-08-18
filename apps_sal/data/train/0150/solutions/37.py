class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)

        partidx = 0
        left_max = A[0]
        seen_max = A[0]
        for i in range(1, n):
            seen_max = max(seen_max, A[i])
            if A[i] < left_max:
                partidx = i
                left_max = seen_max
        return partidx + 1
