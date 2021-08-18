class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
        mini = [float('-inf')] * n
        maxi = [float('inf')] * n
        mini[0] = A[0]
        maxi[n - 1] = A[n - 1]
        for i in range(1, n):
            mini[i] = max(mini[i - 1], A[i])

        for i in range(n - 2, -1, -1):
            maxi[i] = min(maxi[i + 1], A[i])

        for i in range(n - 1):
            if mini[i] <= maxi[i + 1]:
                return i + 1

        return 0
