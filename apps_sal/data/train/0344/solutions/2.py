class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        H, W = len(A), len(A[0])

        def is_valid(j1: int, j2: int) -> bool:
            for i in range(H):
                if A[i][j1] > A[i][j2]:
                    return False
            return True
        f = [1 for _ in range(W)]
        max_v = 1
        for i in reversed(range(W - 1)):
            for j in range(i + 1, W):
                if is_valid(i, j):
                    f[i] = max(f[i], f[j] + 1)
            max_v = max(max_v, f[i])
        print(f)
        return W - max_v
