class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        cache = {}

        def recur(A, B, i, j):
            key = str(i) + '$' + str(j)
            if key in cache:
                return cache[key]
            if i >= len(A) or j >= len(B):
                cache[key] = 0
                return cache[key]
            if A[i] == B[j]:
                cache[key] = 1 + recur(A, B, i + 1, j + 1)
            else:
                cache[key] = max(recur(A, B, i + 1, j), recur(A, B, i, j + 1))
            return cache[key]
        return recur(A, B, 0, 0)
