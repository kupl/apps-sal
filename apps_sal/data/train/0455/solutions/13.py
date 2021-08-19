class Solution:
    def isPrintable(self, M: List[List[int]]) -> bool:
        colorAreas = collections.defaultdict(lambda: [61, 61, -1, -1])  # (top, left, bottom, right)
        for r, row in enumerate(M):
            for c, color in enumerate(row):
                colorAreas[color][0] = min(colorAreas[color][0], r)
                colorAreas[color][1] = min(colorAreas[color][1], c)
                colorAreas[color][2] = max(colorAreas[color][2], r)
                colorAreas[color][3] = max(colorAreas[color][3], c)
        graph = {color: set() for color in colorAreas}
        for color, (top, left, bottom, right) in list(colorAreas.items()):
            for r in range(top, bottom + 1):
                for c in range(left, right + 1):
                    if M[r][c] != color:
                        graph[color].add(M[r][c])
        W, G, B = 0, 1, 2
        state = collections.defaultdict(int)

        def check(node):
            state[node] = G
            for nei in graph[node]:
                if state[nei] == W:
                    if not check(nei):
                        return False
                if state[nei] == G:
                    return False
            state[node] = B
            return True
        for node in graph:
            if state[node] == W:
                if not check(node):
                    return False
        return True
