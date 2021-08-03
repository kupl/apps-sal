def mat_to_set(A):
    return {(i, j) for i, row in enumerate(A) for j, bit in enumerate(row) if bit}


class Solution:
    def largestOverlap(self, A, B) -> int:
        offsets = range(1 - len(A), len(A))
        A, B = mat_to_set(A), mat_to_set(B)

        if len(A) > len(B):
            A, B = B, A

        def overlap(di, dj):
            count = 0
            for i, j in A:
                if (i + di, j + dj) in B:
                    count += 1
            return count

        return max(overlap(di, dj) for di in offsets for dj in offsets)
