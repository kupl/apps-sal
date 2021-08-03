class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        counts, best = {}, 0
        size = len(A[0])
        for x1 in range(size):
            for y1 in range(size):
                if A[y1][x1] == 1:
                    for x2 in range(size):
                        for y2 in range(size):
                            if B[y2][x2] == 1:
                                diff = (x2 - x1, y2 - y1)
                                counts[diff] = counts.get(diff, 0) + 1
                                best = counts[diff] if counts[diff] > best else best
        return best
