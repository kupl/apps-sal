class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        A = list(A)
        B = list(B)

        n = len(A)

        def rec(i):
            if i == n:
                return 0

            if A[i] == B[i]:
                return rec(i + 1)
            else:
                min_ = sys.maxsize
                for j in range(i + 1, n):
                    if B[j] == A[i] and B[j] != A[j]:
                        B[i], B[j] = B[j], B[i]
                        min_ = min(min_, rec(i + 1) + 1)
                        B[i], B[j] = B[j], B[i]
                return min_

        return rec(0)
