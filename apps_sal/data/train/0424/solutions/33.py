class Solution:
    def largestOverlap(self, A, B):
        A = [(i, j) for i, row in enumerate(A) for j, item in enumerate(row) if item]
        B = [(i, j) for i, row in enumerate(B) for j, item in enumerate(row) if item]

        count = {}
        for ax, ay in A:
            for bx, by in B:
                delta = (ax - bx, ay - by)
                if not delta in count:
                    count[delta] = 0
                count[delta] += 1
        return max(count.values()) if count else 0
