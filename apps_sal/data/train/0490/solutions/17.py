class Solution:

    def canVisitAllRooms(self, rooms):
        graph = {}
        visited = {}
        for (node, edges) in enumerate(rooms):
            visited[node] = False
            graph[node] = []
            for edge in edges:
                graph[node].append(edge)

        def DFS(visited, graph, node):
            visited[node] = True
            for neighbour_node in graph[node]:
                if not visited[neighbour_node]:
                    DFS(visited, graph, neighbour_node)
        islands = 0
        for node in visited:
            if not visited[node]:
                islands += 1
                DFS(visited, graph, node)
        return islands == 1
