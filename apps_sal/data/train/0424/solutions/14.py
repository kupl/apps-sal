def mat_to_set(A):
    return {(i, j) for (i, row) in enumerate(A) for (j, bit) in enumerate(row) if bit}


class Solution:

    def largestOverlap(self, A, B) -> int:
        N = len(A)
        (A, B) = (mat_to_set(A), mat_to_set(B))
        if len(A) > len(B):
            (A, B) = (B, A)
        max_overlap = 0
        for di in range(1 - N, N):
            for dj in range(1 - N, N):
                overlap = 0
                for (i, j) in A:
                    if (i + di, j + dj) in B:
                        overlap += 1
                max_overlap = max(max_overlap, overlap)
        return max_overlap
