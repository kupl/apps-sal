class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
        memo = [[0 for _ in range(n)] for _ in range(2)]
        (left, right) = (0, (1 << 31) - 1)
        (i, j) = (0, n - 1)
        while i < n and j >= 0:
            right = min(right, A[j])
            left = max(left, A[i])
            memo[0][i] = left
            memo[1][j] = right
            i += 1
            j -= 1
        (i, j) = (0, 1)
        while j < n and memo[0][i] > memo[1][j]:
            (i, j) = (i + 1, j + 1)
        return j
