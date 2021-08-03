class Component:
    def __init__(self, color):
        self.cells = set()
        self.color = color
        self.min_row = float('inf')
        self.max_row = float('-inf')
        self.min_col = float('inf')
        self.max_col = float('-inf')

    def add_cell(self, u):
        self.cells.add(u)
        self.min_row = min(self.min_row, u[0])
        self.max_row = max(self.max_row, u[0])
        self.min_col = min(self.min_col, u[1])
        self.max_col = max(self.max_col, u[1])

    def remove_cell(self, u):
        self.cells.remove(u)


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        grid = targetGrid

        def discover_components():
            components = {}
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    color = grid[i][j]
                    if color not in components:
                        components[color] = Component(color)
                    components[color].add_cell((i, j))
            return components

        def is_rectangular(c):
            for i in range(c.min_row, c.max_row + 1):
                for j in range(c.min_col, c.max_col + 1):
                    if grid[i][j] != c.color:
                        return False
            return True

        def replace_holes(cx, marked_for_removal):
            # Go through cells from components marked for removal and see if the
            # holes in cx could be replaced with the cells that we will remove
            for i in range(cx.min_row, cx.max_row + 1):
                hole_colors = set()
                for j in range(cx.min_col, cx.max_col + 1):
                    if grid[i][j] == cx.color:
                        continue
                    if grid[i][j] not in marked_for_removal:
                        return

            for i in range(cx.min_row, cx.max_row + 1):
                for j in range(cx.min_col, cx.max_col + 1):
                    if grid[i][j] != cx.color:
                        cx.add_cell((i, j))
                        hc = grid[i][j]
                        marked_for_removal[hc].remove_cell((i, j))
                        if len(marked_for_removal[hc].cells) == 0:
                            del(marked_for_removal[hc])
                        grid[i][j] = cx.color

        components = discover_components()
        marked_for_removal = {}
        while len(components) > 0:
            found_new_comp_to_remove = False
            for c in components:
                if is_rectangular(components[c]):
                    marked_for_removal[c] = components[c]
                    del(components[c])
                    found_new_comp_to_remove = True
                    break
            if not found_new_comp_to_remove:
                return False

            for c in list(components.keys()):
                replace_holes(components[c], marked_for_removal)

        return True
