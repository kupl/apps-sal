class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        ab_dict = {a: [] for a in A}
        for (i, b) in enumerate(B):
            if b in ab_dict:
                ab_dict[b].append(i)
        (lenA, lenB) = (len(A), len(B))
        subSolutions = [[None] * lenB for _ in range(lenA)]

        def subSolve(i, j):
            if i >= lenA or j >= lenB:
                return 0
            if subSolutions[i][j]:
                return subSolutions[i][j]
            if not ab_dict[A[i]]:
                subSolutions[i][j] = 0
                return subSolve(i + 1, j)
            if A[i] in ab_dict and j in ab_dict[A[i]]:
                subSolutions[i][j] = 1 + subSolve(i + 1, j + 1)
                return subSolutions[i][j]
            next_j = None
            for b in ab_dict[A[i]]:
                if j < b:
                    next_j = b
                    break
            if next_j is None:
                subSolutions[i][j] = 0
                return subSolve(i + 1, j)
            subSolutions[i][j] = max(subSolve(i, next_j), subSolve(i + 1, j))
            return subSolutions[i][j]
        return subSolve(0, 0)
