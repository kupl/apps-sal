class Solution:

    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        boundaries = [(math.inf, math.inf, -math.inf, -math.inf) for _ in range(61)]
        for i in range(len(targetGrid)):
            for j in range(len(targetGrid[i])):
                color = targetGrid[i][j]
                (min_i, min_j, max_i, max_j) = boundaries[color]
                boundaries[color] = (min(min_i, i), min(min_j, j), max(max_i, i), max(max_j, j))
        graph = defaultdict(set)
        for color in range(len(boundaries)):
            (min_i, min_j, max_i, max_j) = boundaries[color]
            if min_i != math.inf:
                for i in range(min_i, max_i + 1):
                    for j in range(min_j, max_j + 1):
                        if targetGrid[i][j] != color:
                            graph[color].add(targetGrid[i][j])
        visited = set()
        in_progress = set()

        def dfs(source):
            in_progress.add(source)
            for vertex in graph[source]:
                if vertex in in_progress or (vertex not in visited and (not dfs(vertex))):
                    return False
            in_progress.remove(source)
            visited.add(source)
            return True
        for color in range(61):
            if color not in visited and (not dfs(color)):
                return False
        return True
