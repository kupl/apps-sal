class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = []
        self.dfs(rooms, 0)
        return len(self.visited) == len(rooms)

    def dfs(self, rooms, room_id):
        if room_id in self.visited:
            return
        self.visited.append(room_id)
        for key in rooms[room_id]:
            self.dfs(rooms, key)
