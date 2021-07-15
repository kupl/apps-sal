class Solution:
    # Time Onm
    # Space Onm
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        l1, l2 = len(A), len(B)
        lcs = [[0] * (l1+1) for _ in range(l2+1)]
        # print(lcs)
        for i in range(1, l2+1):
            for j in range(1, l1+1):
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], lcs[i-1][j-1]+(B[i-1]==A[j-1]))
        return lcs[l2][l1]

