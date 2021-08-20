SIDE_LEFT = 'left'
SIDE_RIGHT = 'right'
SIDE_TOP = 'top'
SIDE_BOTTOM = 'bottom'


class Solution:

    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        colour_set = set()
        for row in targetGrid:
            for cell in row:
                colour_set.add(cell)
        colour_overlap_info = self.get_colour_boundaries_and_overlap(targetGrid, colour_set)
        remaining_colours = colour_set.copy()
        untangled_colours = set()
        while remaining_colours:
            new_untangled_colours = set()
            for colour in remaining_colours:
                colour_overlap_info[colour] -= untangled_colours
                if len(colour_overlap_info[colour]) == 0:
                    new_untangled_colours.add(colour)
            if new_untangled_colours:
                untangled_colours |= new_untangled_colours
                remaining_colours -= new_untangled_colours
            else:
                break
        return len(remaining_colours) == 0

    def get_colour_boundaries_and_overlap(self, targetGrid, colour_set):
        colours_info = {}
        for colour in colour_set:
            boundaries = {}
            for (row_index, row) in enumerate(targetGrid):
                for (col_index, cell) in enumerate(row):
                    if cell == colour:
                        if not boundaries:
                            boundaries = {SIDE_LEFT: col_index, SIDE_RIGHT: col_index, SIDE_TOP: row_index, SIDE_BOTTOM: row_index}
                        else:
                            if boundaries[SIDE_LEFT] > col_index:
                                boundaries[SIDE_LEFT] = col_index
                            if boundaries[SIDE_RIGHT] < col_index:
                                boundaries[SIDE_RIGHT] = col_index
                            if boundaries[SIDE_BOTTOM] < row_index:
                                boundaries[SIDE_BOTTOM] = row_index
            overlapping_colours = set()
            for row_index in range(boundaries[SIDE_TOP], boundaries[SIDE_BOTTOM] + 1):
                for col_index in range(boundaries[SIDE_LEFT], boundaries[SIDE_RIGHT] + 1):
                    cell = targetGrid[row_index][col_index]
                    if cell != colour:
                        overlapping_colours.add(cell)
            colours_info[colour] = overlapping_colours
        return colours_info
