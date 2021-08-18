class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        size = len(A[0])
        best = [0] * size
        best[0] = 1
        for i in range(1, size):
            best[i] = 1
            for j in range(0, i):
                if best[j] >= best[i] and self.beats(A, i, j):
                    best[i] = best[j] + 1

        return size - max(best)

    def beats(self, A, a, b):
        for s in A:
            if s[b] > s[a]:
                return False

        return True
