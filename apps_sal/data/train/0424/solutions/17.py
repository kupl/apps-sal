class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        max_count = 0

        a_coords = self.coordinates(A)
        b_coords = self.coordinates(B)

        for v in range(-1 * (len(A) - 1), len(A)):
            for h in range(-1 * (len(A[0]) - 1), len(A[0])):
                overlap_count = 0
                for r, c in a_coords:
                    if (r + v, c + h) in b_coords:
                        overlap_count += 1

                max_count = max(max_count, overlap_count)

        return max_count

    def coordinates(self, image):
        coords = set()
        for r, row in enumerate(image):
            for c, value in enumerate(row):
                if value == 1:
                    coords.add((r, c))
        return coords
