class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        index_A = [(i, j) for i, row in enumerate(A) for j, item in enumerate(row) if item]
        index_B = [(i, j) for i, row in enumerate(B) for j, item in enumerate(row) if item]

        cnt = collections.Counter([(ax - bx, ay - by)for ax, ay in index_A for bx, by in index_B])

        if len(cnt) == 0:
            return 0
        return max(cnt.values())
