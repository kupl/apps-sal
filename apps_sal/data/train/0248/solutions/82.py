from collections import deque


class Solution:

    def __init__(self):
        self.locs = defaultdict(set)
        self.grid = []

    def isValid(self, i, j):
        return i >= 0 and i < len(self.grid) and j >= 0 and j < len(self.grid[i])

    def hasCycle(self, l):
        seen = set()
        todo = deque([])
        around = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for x in l:
            if x not in seen:
                todo.append([(-1, -1), x])
                while todo:
                    node = todo.popleft()
                    cur = node[1]
                    fr = node[0]
                    if cur in seen:

                        return True
                    seen.add(cur)
                    for x in around:
                        test = (cur[0] + x[0], cur[1] + x[1])
                        if self.isValid(test[0], test[1]) and test in l and not test == fr:

                            todo.append([cur, test])
        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.grid = grid
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                self.locs[grid[x][y]].add((x, y))
        for x in list(self.locs.keys()):
            if self.hasCycle(self.locs[x]):
                return True
        return False
