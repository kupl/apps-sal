class Solution:
    # Naming assumes row major.
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        # move A through all the valid positions in B's coordinate space.
        a_1_locations = set()
        b_1_locations = set()

        for grid, locations in [(A, a_1_locations), (B, b_1_locations)]:
            for i, col in enumerate(grid):
                for j, val in enumerate(col):
                    if val == 1:
                        locations.add((i, j))

        max_overlap = 0
        max_abs_x1_offset = len(A)
        max_abs_x2_offset = len(A[0])
        a_offsets = itertools.product(range(-1 * max_abs_x1_offset, max_abs_x1_offset),
                                      range(-1 * max_abs_x2_offset, max_abs_x2_offset))

        for a_offset_x, a_offset_y in a_offsets:
            a_1_locations_offset = set(map(lambda location: (location[0] + a_offset_x, location[1] + a_offset_y),
                                           a_1_locations))
            overlap = len(a_1_locations_offset & b_1_locations)
            if overlap > max_overlap:
                max_overlap = overlap

        return max_overlap
