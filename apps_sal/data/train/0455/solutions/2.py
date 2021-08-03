class Solution:
    from collections import defaultdict, Counter

    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        shapes = {}  # color: [min_r, max_r, min_c, max_c]

        for i, row in enumerate(targetGrid):
            for j, color in enumerate(row):
                if color not in shapes:
                    shapes[color] = [i, i, j, j]
                else:
                    shapes[color][0] = min(shapes[color][0], i)
                    shapes[color][1] = max(shapes[color][1], i)
                    shapes[color][2] = min(shapes[color][2], j)
                    shapes[color][3] = max(shapes[color][3], j)

        edges = defaultdict(set)

        for color, [min_r, max_r, min_c, max_c] in list(shapes.items()):
            for r in range(min_r, max_r + 1):
                for c in range(min_c, max_c + 1):
                    if targetGrid[r][c] != color:
                        edges[color].add(targetGrid[r][c])

        deps = Counter()
        for _, ts in list(edges.items()):
            for c in ts:
                deps[c] += 1

        layer = [c for c in list(shapes.keys()) if not deps[c]]
        while layer:
            new_layer = []
            for c in layer:
                for t in edges[c]:
                    deps[t] -= 1
                    if not deps[t]:
                        new_layer.append(t)
            layer = new_layer

        return all(not v for c, v in list(deps.items()))
