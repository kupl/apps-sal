class Solution:
    dbg = False

    def minSwaps(self, grid) -> int:
        grid_ints = []
        for row in grid:
            enc = 0
            for val in reversed(row):
                enc = enc << 1
                if val % 2 == 1:
                    enc += 1
            grid_ints.append(enc)
        if self.dbg:
            print(grid_ints)
        bar = 1
        swaps = 0
        for i in range(len(grid[0])):
            if grid_ints[i] > bar:
                j = i
                while grid_ints[j] > bar:
                    j += 1
                    if j >= len(grid[0]):
                        return -1
                while j > i:
                    (grid_ints[j], grid_ints[j - 1]) = (grid_ints[j - 1], grid_ints[j])
                    swaps += 1
                    j -= 1
            bar = (bar << 1) + 1
        return swaps
