class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        (prev, crnt) = ([0] * (1 + len(B)), [0] * (1 + len(B)))
        for a in range(len(A)):
            (prev, crnt) = (crnt, prev)
            for b in range(len(B)):
                if A[a] == B[b]:
                    crnt[b + 1] = prev[b] + 1
                else:
                    crnt[b + 1] = max(crnt[b], prev[b + 1])
        return crnt[len(B)]
