class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        def check_overlap(side_x, down_x, A, B):
            overlap = 0
            for i in range(len(A)):
                for j in range(len(A)):
                    try:
                        overlap += A[i + side_x][j + down_x] & B[i][j]
                    except:
                        pass

            return overlap

        max_overlap = 0
        for i in range(len(A)):
            for j in range(len(A)):
                max_overlap = max(max_overlap, check_overlap(i, j, A, B))
                max_overlap = max(max_overlap, check_overlap(i, j, B, A))

        return max_overlap
