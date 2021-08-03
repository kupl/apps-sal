class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def recur(room, visited):
            if room in visited:
                return False
            visited.append(room)
            if len(visited) == len(rooms):
                return True
            for i in rooms[room]:
                if recur(i, visited):
                    return True
            return False

        return recur(0, [])
