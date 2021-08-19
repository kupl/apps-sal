class Solution:
    def isPrintable(self, M: List[List[int]]) -> bool:
        colorA = collections.defaultdict(lambda: [61, 61, -1, -1])  # (top, left, bottom, right)
        for r, row in enumerate(M):
            for c, color in enumerate(row):
                colorA[color][0] = min(colorA[color][0], r)
                colorA[color][1] = min(colorA[color][1], c)
                colorA[color][2] = max(colorA[color][2], r)
                colorA[color][3] = max(colorA[color][3], c)
        graph = {color: set() for color in colorA}
        for color, (top, left, bottom, right) in list(colorA.items()):
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
