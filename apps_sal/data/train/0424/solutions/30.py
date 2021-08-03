class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        A = [(i, j) for i, row in enumerate(img1) for j, item in enumerate(row) if item]
        B = [(i, j) for i, row in enumerate(img2) for j, item in enumerate(row) if item]
        count = collections.Counter((ax - bx, ay - by) for ax, ay in A for bx, by in B)
        return max(list(count.values()) or [0])
