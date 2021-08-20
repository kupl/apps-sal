class Solution:

    def binary_search(self, A, k, n):
        lo = 0
        hi = n
        mid = (lo + hi) // 2
        while lo < hi:
            if A[k - 1][mid - 1] == A[k][n - mid]:
                return mid
            if A[k - 1][mid - 1] > A[k][n - mid]:
                hi = mid
            else:
                lo = mid + 1
            mid = (lo + hi) // 2
        return lo

    def superEggDrop(self, K: int, N: int) -> int:
        if K == 1:
            return N
        A = [n + 1 for n in range(N)]
        At = [1 for n in range(N)]
        for k in range(1, K):
            i = 0
            while At[i] < N:
                i += 1
                At[i] = At[i - 1] + A[i - 1] + 1
            if k < K - 1:
                (At, A) = (A, At)
        return i + 1
        return A[-1][-1]
