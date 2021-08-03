class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rem_rooms = [i for i in range(1, len(rooms))]

        visited = set()

        def dfs(r, key):
            stack = [key]

            while stack and rem_rooms:
                element = stack.pop()
                if element in rem_rooms:
                    rem_rooms.remove(element)

                if element not in visited:
                    visited.add(element)

                    for neighbour in rooms[element]:
                        stack.append(neighbour)

        dfs(rooms, 0)

        return len(rem_rooms) == 0
