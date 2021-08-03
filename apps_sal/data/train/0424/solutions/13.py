class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        offset_map = {}
        max_overlap = 0
        for row in range(0, len(A)):
            offset_map[row] = {}
            offset_map[row * -1] = {}
            for col in range(0, len(A[row])):
                r_row = row
                r_col = col
                if not offset_map[r_row] or not r_col in offset_map[r_row] or not offset_map[r_row][r_col]:
                    overlap = self.shift_and_count(A, B, r_row, r_col)
                    overlap = max(overlap, self.shift_and_count(B, A, r_row, r_col))
                    max_overlap = max(overlap, max_overlap)
                    offset_map[r_row][r_col] = overlap
        return max_overlap

    def shift_and_count(self, A: List[List[int]], B: List[List[int]], row_shift: int, col_shift: int) -> int:
        result = 0
        for row in range(len(A)):
            new_row = row - row_shift
            if new_row >= 0 and new_row < len(A):
                for col in range(len(A[row])):
                    new_col = col - col_shift
                    if ((new_col >= 0 and new_col < len(A[row]))):
                        if (A[new_row][new_col] == 1) and B[row][col] == 1:
                            result += 1

        return result

    def overlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        overlap = 0
        if len(A) != len(B):
            raise ValueError
        for row in range(0, len(A)):
            for col in range(0, len(A[row])):
                if len(A[row]) != len(B[row]):
                    raise ValueError
                if A[row][col] == 1 and B[row][col] == 1:
                    overlap += 1
        return overlap
