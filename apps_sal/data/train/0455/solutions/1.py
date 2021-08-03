SIDE_LEFT = 'left'
SIDE_RIGHT = 'right'
SIDE_TOP = 'top'
SIDE_BOTTOM = 'bottom'


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:

        # Step 1: Get the set of the different colours being used
        colour_set = set()
        for row in targetGrid:
            for cell in row:
                colour_set.add(cell)

        # Step 2: Determine the size of each rectangle and the colours that overlap
        colour_overlap_info = self.get_colour_boundaries_and_overlap(targetGrid, colour_set)
        #print(colour_set, colour_overlap_info)

        # Step 3: Loop over the overlapping info. With each pass, print from the last colours downward. In this way, we'll determine
        # which colours we will print going backwards. If we can't print a colour underneath in an iteration, we've failed
        remaining_colours = colour_set.copy()
        untangled_colours = set()
        while remaining_colours:
            new_untangled_colours = set()
            for colour in remaining_colours:
                # Remove any colours that have been untangled
                colour_overlap_info[colour] -= untangled_colours
                if len(colour_overlap_info[colour]) == 0:
                    # We just untangled this one!
                    new_untangled_colours.add(colour)

            # Check if we've untangled anything new. If not, exit
            # print(new_untangled_colours)
            if new_untangled_colours:
                untangled_colours |= new_untangled_colours  # Add them to the full set
                remaining_colours -= new_untangled_colours  # Remove them from the full list
            else:
                break

        return len(remaining_colours) == 0  # If we've untangled everything, there are no remaining colours and it can be printed

    def get_colour_boundaries_and_overlap(self, targetGrid, colour_set):
        # Determine the size of each rectangle and the colours that overlap
        colours_info = {}
        for colour in colour_set:

            # Get the boundaries
            boundaries = {}
            for row_index, row in enumerate(targetGrid):
                for col_index, cell in enumerate(row):
                    if cell == colour:
                        # Update the boundaries
                        if not boundaries:
                            # Initialize
                            boundaries = {
                                SIDE_LEFT: col_index,
                                SIDE_RIGHT: col_index,
                                SIDE_TOP: row_index,
                                SIDE_BOTTOM: row_index
                            }
                        else:
                            # Update the boundaries. Note that top can't move but left can
                            if boundaries[SIDE_LEFT] > col_index:
                                boundaries[SIDE_LEFT] = col_index
                            if boundaries[SIDE_RIGHT] < col_index:
                                boundaries[SIDE_RIGHT] = col_index
                            if boundaries[SIDE_BOTTOM] < row_index:
                                boundaries[SIDE_BOTTOM] = row_index
            #print(colour, boundaries)

            # Now that we have the boundaries, get the colours inside them
            overlapping_colours = set()
            for row_index in range(boundaries[SIDE_TOP], boundaries[SIDE_BOTTOM] + 1):
                for col_index in range(boundaries[SIDE_LEFT], boundaries[SIDE_RIGHT] + 1):
                    cell = targetGrid[row_index][col_index]
                    if cell != colour:
                        overlapping_colours.add(cell)

            # Save the data
            colours_info[colour] = overlapping_colours

        return colours_info
