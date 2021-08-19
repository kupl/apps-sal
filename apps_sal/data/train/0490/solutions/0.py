class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(node, visited):
            if node in visited:
                return
            visited.add(node)
            for nei in rooms[node]:
                if nei in visited:
                    continue
                dfs(nei, visited)
            return
        visited = set()
        dfs(0, visited)
        if len(visited) == len(rooms):
            return True
        else:
            return False
