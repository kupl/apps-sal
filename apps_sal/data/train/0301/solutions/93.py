class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if len(A) < len(B):
            (A, B) = (B, A)
        DP = [0] * (len(A) + 1)
        coll = {j: [-1] + [i for i in range(len(A)) if A[i] == j] for j in set(B)}
        for iB in B[::-1]:
            for i in range(1, len(coll[iB])):
                DP[coll[iB][i]] = max(DP[coll[iB][i]], DP[coll[iB][i] + 1] + 1)
                for j in range(coll[iB][i], coll[iB][i - 1], -1):
                    DP[j] = max(DP[j], DP[j + 1])
        return DP[0]
