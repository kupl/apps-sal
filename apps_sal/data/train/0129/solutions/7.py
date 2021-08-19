class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # consider B[i] = A[i] + i, C[i] = A[i] -j
        # Find the B[i] + C[j]
        B = [A[i] + i for i in range(len(A))]
        C = [A[i] - i for i in range(len(A))]
        p = 0
        q = 1
        max_score = float('-inf')
        # for each q = 1, 2,..., len(A) - 1
        # update the max of B[0], ...., B[j-1]: B[p]
        # calculate B[q] - B[p]
        while q < len(B):
            if B[q - 1] > B[p]:
                p = q - 1
            max_score = max(max_score, B[p] + C[q])
            q += 1
        return max_score
