class Grid(object):

    def __init__(self):
        self.ps = set()
        self.lx = 100
        self.ly = 100
        self.rx = 0
        self.ry = 0

    def add(self, x, y):
        self.ps.add((x, y))
        self.lx = min(self.lx, x)
        self.ly = min(self.ly, y)
        self.rx = max(self.rx, x)
        self.ry = max(self.ry, y)

    def is_full(self):
        return len(self.ps) == (self.rx - self.lx + 1) * (self.ry - self.ly + 1)

    def overlap(self, grid):
        flag = self.rx < grid.lx
        flag = flag and self.ry > grid.ly
        flag = flag and self.lx > grid.rx
        flag = flag and self.ly < grid.ry
        return not flag

    def contain(self, grid):
        if not self.overlap(grid):
            return False
        for (x, y) in grid.ps:
            if self.lx <= x <= self.rx and self.ly <= y <= self.ry:
                return True
        return False

    def __str__(self):
        return '({0.lx}, {0.ly}), ({0.rx}, {0.ry})'.format(self)


class Solution:

    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        grids = defaultdict(Grid)
        for (x, row) in enumerate(targetGrid):
            for (y, c) in enumerate(row):
                grids[c].add(x, y)
        colors = grids.keys()
        (graph, degree) = (defaultdict(set), defaultdict(int))
        vis = set()
        for c1 in colors:
            for c2 in colors:
                if c1 == c2 or (c1, c2) in vis:
                    continue
                vis.add((c1, c2))
                if grids[c1].contain(grids[c2]):
                    graph[c1].add(c2)
                    degree[c2] += 1
        q = []
        for c in colors:
            if degree[c] == 0:
                q.append(c)
        vis = []
        while q:
            c1 = q.pop()
            vis.append(c1)
            for c2 in graph[c1]:
                degree[c2] -= 1
                if degree[c2] == 0:
                    q.append(c2)
        return len(vis) == len(colors)
