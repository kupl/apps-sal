class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        for (x, row) in enumerate(grid):
            for (y, num) in enumerate(row):
                if self.containsCycleInComponent(grid, (x, y)):
                    return True
        return False

    def adjCells(self, x, y):
        yield (x - 1, y)
        yield (x + 1, y)
        yield (x, y - 1)
        yield (x, y + 1)

    def containsCycleInComponent(self, grid, startPoint):
        (startX, startY) = startPoint
        value = grid[startX][startY]
        if value is None:
            return False
        checkedPoints = set()
        uncheckedPoints = [startPoint]
        while uncheckedPoints:
            point = uncheckedPoints.pop()
            checkedPoints.add(point)
            (x, y) = point
            grid[x][y] = None
            adjKnownPoints = 0
            for nextPoint in self.adjCells(x, y):
                if nextPoint in checkedPoints or self.hasValue(grid, nextPoint, value):
                    if nextPoint not in checkedPoints:
                        uncheckedPoints.append(nextPoint)
                    else:
                        adjKnownPoints += 1
            if adjKnownPoints > 1:
                return True
        return False

    def hasValue(self, grid, point, value):
        (x, y) = point
        return 0 <= x < len(grid) and 0 <= y < len(grid[x]) and (grid[x][y] == value)
