class Solution:
    def isPrintable(self, target: List[List[int]]) -> bool:
        TOP, LEFT, BOTTOM, RIGHT = 0, 1, 2, 3
        M, N = len(target), len(target[0])
        boxes = defaultdict(lambda: [math.inf, math.inf, -math.inf, -math.inf])
        for i, row in enumerate(target):
            for j, x in enumerate(row):
                boxes[x][TOP] = min(boxes[x][TOP], i)
                boxes[x][LEFT] = min(boxes[x][LEFT], j)
                boxes[x][BOTTOM] = max(boxes[x][BOTTOM], i)
                boxes[x][RIGHT] = max(boxes[x][RIGHT], j)
        graph = {color: set() for color in boxes}
        for color, (i1, j1, i2, j2) in boxes.items():
            for i in range(i1, i2 + 1):
                for j in range(j1, j2 + 1):
                    if target[i][j] != color:
                        graph[color].add(target[i][j])
        WHITE, GRAY, BLACK = 0, 1, 2
        color = defaultdict(int)

        def dfs(u):
            color[u] = GRAY
            for v in graph[u]:
                if color[v] == GRAY:
                    return False
                elif color[v] == WHITE and not dfs(v):
                    return False
            color[u] = BLACK
            return True

        return all(color[u] == BLACK or dfs(u) for u in graph)
