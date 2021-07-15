class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], probs: List[float], s: int, t: int) -> float:
        # first build the graph
        graph = {u: {} for u in range(n)}
        for (u, v), prob in zip(edges, probs):
            graph[u][v] = prob
            graph[v][u] = prob

        # run DFS/BFS search
        frontier = [s]
        path_probs = {u: 0 for u in range(n)}
        path_probs[s] = 1

        while len(frontier) != 0:
            u = frontier.pop(0)
            path_prob = path_probs[u]

            for v, edge_prob in graph[u].items():
                if path_prob * edge_prob > path_probs[v]:
                    path_probs[v] = path_prob * edge_prob
                    frontier.append(v)
        return path_probs[t]
