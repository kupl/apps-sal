class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        R = len(targetGrid)
        C = len(targetGrid[0])
        WHITE = 0
        GRAY = 1
        BLACK = 2
        boxes = collections.defaultdict(lambda: [61, 61, -1, -1])

        for r, row in enumerate(targetGrid):
            for c, v in enumerate(row):
                boxes[v][0] = min(boxes[v][0], r)
                boxes[v][1] = min(boxes[v][1], c)
                boxes[v][2] = max(boxes[v][2], r)
                boxes[v][3] = max(boxes[v][3], c)

        graph = {color: set() for color in boxes}

        for color, (r1, c1, r2, c2) in boxes.items():
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if targetGrid[r][c] != color:
                        graph[color].add(targetGrid[r][c])

        state = collections.defaultdict(int)

        def dfs(u):
            state[u] = GRAY

            for v in graph[u]:
                if state[v] == WHITE:
                    if not dfs(v):
                        return False
                elif state[v] == GRAY:
                    return False

            state[u] = BLACK
            return True

        for s in graph:
            if state[s] == WHITE:
                if not dfs(s):
                    return False

        return True
