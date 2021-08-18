class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        B = [A[i] + i for i in range(len(A))]
        C = [A[i] - i for i in range(len(A))]
        p = 0
        q = 1
        max_score = 0
        while q < len(B):
            if B[q - 1] > B[p]:
                p = q - 1
            max_score = max(max_score, B[p] + C[q])
            q += 1
        return max_score
