class Room:

    def __init__(self, num, keys):
        self.num = num
        self.keys = keys
        self.visited = False


class Solution:

    def explore(self, room_id, all_rooms):
        cur_room = all_rooms[room_id]
        if cur_room.visited:
            return
        cur_room.visited = True
        for key in cur_room.keys:
            self.explore(key, all_rooms)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        all_rooms = [Room(i, keys) for (i, keys) in enumerate(rooms)]
        self.explore(0, all_rooms)
        for room in all_rooms:
            if not room.visited:
                return False
        return True
