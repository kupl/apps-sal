class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        n = len(A)
        A = list(A)
        B = list(B)

        base = 0
        for i in range(n):
            if A[i] == B[i]:
                continue

            for j in range(i + 1, n):
                if A[i] == B[j] and A[j] == B[i]:
                    A[i], A[j] = A[j], A[i]
                    base += 1
                    break

        # invariant: A[:i] == B[:i]
        def dfs(i):
            if i == n:
                return 0

            if A[i] == B[i]:
                return dfs(i + 1)

            desired = B[i]
            cand = float('inf')
            for j in range(i + 1, n):
                if A[j] == desired:
                    A[i], A[j] = A[j], A[i]
                    cand = min(cand, 1 + dfs(i + 1))
                    A[i], A[j] = A[j], A[i]

            return cand

        return base + dfs(0)
