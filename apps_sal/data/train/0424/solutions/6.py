class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        def nonzero_cells(matrix):
            ones = []
            for r in range(len(matrix)):
                for c in range(len(matrix[r])):
                    if matrix[r][c] == 1:
                        ones.append((r, c))
            return ones

        a = nonzero_cells(A)
        b = nonzero_cells(B)
        overlap_vectors = defaultdict(int)

        max_overlap = 0
        for x_a, y_a in a:
            for x_b, y_b in b:
                overlap_vector = ((x_b - x_a, y_b - y_a))
                overlap_vectors[overlap_vector] += 1
                max_overlap = max(max_overlap, overlap_vectors[overlap_vector])

        return max_overlap
