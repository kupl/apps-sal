class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        A_map = {x: i for i, x in enumerate(A)}

        M = [[2] * len(A) for _ in range(len(A))]

        best = 0
        for k in range(2, len(A)):
            for j in range(1, k):
                i = A_map.get(A[k] - A[j], None)
                if i is not None and i < j:
                    M[j][k] = M[i][j] + 1
                    best = max(best, M[j][k])

        return best if best >= 3 else 0
