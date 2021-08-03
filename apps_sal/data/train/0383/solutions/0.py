from collections import deque


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:

        def bfs(graph, seed, removed):
            queue = deque(seed)
            visited = seed

            while len(queue) > 0:
                node = queue.popleft()
                for next_node in range(len(graph[node])):
                    if graph[node][next_node] == 0 or next_node in visited or next_node == removed:
                        continue
                    visited.add(next_node)
                    queue.append(next_node)
            return len(visited)

        best = len(graph)
        best_remove = initial[0]
        initial = set(initial)

        for remove_node in initial:
            initial_removed = initial - {remove_node}
            node_result = bfs(graph, initial_removed, remove_node)

            if (node_result < best) or (node_result == best) and (best_remove > remove_node):
                best = node_result
                best_remove = remove_node
        return best_remove
