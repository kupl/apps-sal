class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        if not grid:
            return False
        visited = [[0 for i in grid[0]] for j in grid]

        def ExplorePath(rowIn, colIn, value, previous):
            current = [rowIn, colIn]
            if visited[rowIn][colIn] == 1:
                return True
            else:
                visited[rowIn][colIn] = 1
                output = False
                if rowIn < len(grid) - 1 and previous != [rowIn + 1, colIn] and (grid[rowIn + 1][colIn] == value):
                    output = ExplorePath(rowIn + 1, colIn, value, current)
                if colIn < len(grid[0]) - 1 and previous != [rowIn, colIn + 1] and (grid[rowIn][colIn + 1] == value):
                    output = output or ExplorePath(rowIn, colIn + 1, value, current)
                if rowIn > 0 and previous != [rowIn - 1, colIn] and (grid[rowIn - 1][colIn] == value):
                    output = output or ExplorePath(rowIn - 1, colIn, value, current)
                if colIn > 0 and previous != [rowIn, colIn - 1] and (grid[rowIn][colIn - 1] == value):
                    output = output or ExplorePath(rowIn, colIn - 1, value, current)
            return output
        for rowIn in range(len(grid) - 1):
            for colIn in range(len(grid[0]) - 1):
                if grid[rowIn + 1][colIn] == grid[rowIn][colIn]:
                    if grid[rowIn + 1][colIn + 1] == grid[rowIn][colIn]:
                        if grid[rowIn][colIn + 1] == grid[rowIn][colIn]:
                            return True
        for rowIn in range(len(grid)):
            for colIn in range(len(grid[0])):
                if visited[rowIn][colIn] == 0:
                    tempVisited = []
                    length = 0
                    if ExplorePath(rowIn, colIn, grid[rowIn][colIn], [rowIn, colIn]):
                        return True
        return False

    def containsCycle2(self, grid: List[List[str]]) -> bool:
        if not grid:
            return False
        visited = [[0 for i in grid[0]] for j in grid]

        def ExplorePath(rowIn, colIn, length, tempV, value, previous):
            current = [rowIn, colIn]
            if grid[rowIn][colIn] != value:
                return False
            if [rowIn, colIn] in tempV:
                if length >= 3:
                    return True
                else:
                    return False
            else:
                tempV.append([rowIn, colIn])
                visited[rowIn][colIn] = 1
                (temp1, temp2, temp3, temp4) = (deepcopy(tempV), deepcopy(tempV), deepcopy(tempV), deepcopy(tempV))
                output = False
                if rowIn < len(grid) - 1 and previous != [rowIn + 1, colIn]:
                    output = ExplorePath(rowIn + 1, colIn, length + 1, temp1, value, current)
                if colIn < len(grid[0]) - 1 and previous != [rowIn, colIn + 1]:
                    output = output or ExplorePath(rowIn, colIn + 1, length + 1, temp2, value, current)
                if rowIn > 0 and previous != [rowIn - 1, colIn]:
                    output = output or ExplorePath(rowIn - 1, colIn, length + 1, temp3, value, current)
                if colIn > 0 and previous != [rowIn, colIn - 1]:
                    output = output or ExplorePath(rowIn, colIn - 1, length + 1, temp4, value, current)
            return output
        for rowIn in range(len(grid) - 1):
            for colIn in range(len(grid[0]) - 1):
                if grid[rowIn + 1][colIn] == grid[rowIn][colIn]:
                    if grid[rowIn + 1][colIn + 1] == grid[rowIn][colIn]:
                        if grid[rowIn][colIn + 1] == grid[rowIn][colIn]:
                            return True
        for rowIn in range(len(grid)):
            for colIn in range(len(grid[0])):
                if visited[rowIn][colIn] == 0:
                    tempVisited = []
                    length = 0
                    if ExplorePath(rowIn, colIn, length, tempVisited, grid[rowIn][colIn], [rowIn, colIn]):
                        return True
        return False
