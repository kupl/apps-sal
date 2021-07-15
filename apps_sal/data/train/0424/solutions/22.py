def matrix_to_set(A):
    return {(i, j) for i, row in enumerate(A)
                   for j, pixel in enumerate(row) if pixel}

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        set_a, set_b = matrix_to_set(A), matrix_to_set(B)
        
        if len(set_b) < len(set_a):
            set_b, set_a = set_a, set_b
    
        return max(sum((i + di, j + dj) in set_b for i, j in set_a)
                   for di in range(-N + 1, N)
                   for dj in range(-N + 1, N)) 

