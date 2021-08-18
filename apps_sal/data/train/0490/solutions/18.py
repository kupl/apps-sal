class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(curRoom, visited):
            visited[curRoom] = True

            for key in rooms[curRoom]:
                if not visited[key]:
                    dfs(key, visited)

        visited = [False] * len(rooms)
        dfs(0, visited)
        return all(visited)
