class Solution:

    def kSimilarity(self, A: str, B: str) -> int:
        A = list(A)
        memo = {}

        def solution(i):
            t = tuple(A)
            if (i, t) in memo:
                return memo[i, t]
            if i == len(A):
                return 0
            if A[i] == B[i]:
                return solution(i + 1)
            mymin = float('inf')
            for j in range(i + 1, len(A)):
                if A[j] != B[i]:
                    continue
                (A[i], A[j]) = (A[j], A[i])
                mymin = min(mymin, solution(i + 1))
                (A[j], A[i]) = (A[i], A[j])
            memo[i, t] = 1 + mymin
            return 1 + mymin
        return solution(0)
