class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        return max(self.largestOverlapAtoB(A, B), self.largestOverlapAtoB(B, A))
        
    def largestOverlapAtoB(self, A, B):
        shift_row = 0
        shift_col = 0
        overlap = 0
        for shift_row in range(len(A[0])):
            for shift_col in range(len(A[0])):
                shifted_A = self.shiftMatrix(A, shift_row, shift_col)
                overlap = max(overlap, self.findOverlap(B, shifted_A))
        return overlap
        
    def findOverlap(self, A, B):
        lenght = len(A[0])
        overlap = 0
        for ii in range(lenght):
            for jj in range(lenght):
                if A[ii][jj] == B[ii][jj] and A[ii][jj] == 1:
                    overlap += 1
        return overlap
    
    def shiftMatrix(self, M, shift_row, shift_col):
        lenght = len(M[0])
        out = []
        for _ in range(shift_row):
            out.append(lenght * [0])
        for ix_r in range(shift_row, lenght):
            out_row = []
            for _ in range(shift_col):
                out_row.append(0)
            for ix_c in range(shift_col, lenght):
                out_row.append(M[ix_r - shift_row][ix_c - shift_col])
                
            out.append(out_row)
        
        return out
                    
                    

