from queue import PriorityQueue


class Solution:
    def isInRange(self, grid, x, y):
        return (0 <= x and x < len(grid[0])) and (0 <= y and y < len(grid))

    def maxDistance(self, grid: List[List[int]]) -> int:
        q = PriorityQueue()
        visited = dict()
        maxDist = 0
        toVisit = [(-1, 0), (0, 0), (1, 0), (0, 1), (0, -1)]

        for x, i in enumerate(grid):
            for y, j in enumerate(i):
                if j is not 0:
                    q.put((0, (x, y)))
                    visited[(x, y)] = True

        if (q.qsize() >= len(grid[0]) * len(grid) or q.qsize() is 0):
            return -1

        while not q.empty():
            item = q.get()
            maxDist = max(maxDist, item[0])

            for p in toVisit:
                x = p[0] + item[1][0]
                y = p[1] + item[1][1]

                if self.isInRange(grid, x, y) and visited.get((x, y)) is not True:
                    visited[(x, y)] = True
                    q.put((item[0] + 1, (x, y)))

        return maxDist
