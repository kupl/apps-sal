class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        def help(i, j, mem):
            if i >= len(A) or j >= len(B):
                return 0
            if (i, j) in mem:
                return mem[i, j]
            if A[i] == B[j]:
                mem[i, j] = 1 + help(i + 1, j + 1, mem)
                return mem[i, j]
            mem[i, j] = max(help(i, j + 1, mem), help(i + 1, j, mem))
            return mem[i, j]
        mem = {}
        return help(0, 0, mem)
