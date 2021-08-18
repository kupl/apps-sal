class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
        d = [0] * n
        d[n - 1] = A[n - 1]
        for i in range(len(A) - 2, -1, -1):
            d[i] = min(A[i], d[i + 1])
        mx = A[0]
        for i in range(1, n):
            if mx <= d[i]:
                return i
            else:
                mx = max(mx, A[i])
