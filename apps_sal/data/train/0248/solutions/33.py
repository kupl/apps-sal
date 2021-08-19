class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        for x, row in enumerate(grid):
            for y, num in enumerate(row):
                if self.containsCycleInComponent(grid, (x, y)):
                    return True
                else:
                    self.eraseComponent(grid, (x, y))

        return False

    def eraseComponent(self, grid, startPoint):
        # startPoint is the position (x,y)
        startX, startY = startPoint
        value = grid[startX][startY]
        if value is None:
            return

        pointsToErase = [startPoint]
        while pointsToErase:
            point = pointsToErase.pop()
            x, y = point
            grid[x][y] = None
            for nextPoint in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if self.hasValue(grid, nextPoint, value):
                    pointsToErase.append(nextPoint)

    def containsCycleInComponent(self, grid, startPoint):
        # startPoint is the position (x,y)
        startX, startY = startPoint
        value = grid[startX][startY]
        if value is None:
            return False

        checkedPoints = set()
        uncheckedPoints = [startPoint]
        componentPointsCount = 0
        componentEdgesDoubleCount = 0

        while uncheckedPoints:
            point = uncheckedPoints.pop()
            componentPointsCount += 1
            checkedPoints.add(point)

            x, y = point
            for nextPoint in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if self.hasValue(grid, nextPoint, value):
                    componentEdgesDoubleCount += 1
                    if nextPoint not in checkedPoints:
                        uncheckedPoints.append(nextPoint)

        return componentPointsCount <= componentEdgesDoubleCount // 2

    def hasValue(self, grid, point, value):
        x, y = point
        return 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] == value
