def mat_to_set(A):
    return {(i, j) for i, row in enumerate(A) for j, bit in enumerate(row) if bit}

def overlap(A, B, di, dj):
    count = 0
    for i, j in A:
        if (i + di, j + dj) in B:
            count += 1
    return count

class Solution:
    def largestOverlap(self, A, B) -> int:
        offsets = range(1 - len(A), len(A))
        A, B = mat_to_set(A), mat_to_set(B)
        
        if len(A) > len(B):
            A, B = B, A
    
        return max(overlap(A, B, di, dj) for di in offsets for dj in offsets)
