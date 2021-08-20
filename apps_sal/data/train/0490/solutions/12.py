class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited = set([0])
        while q:
            r = q.pop()
            for k in rooms[r]:
                if k not in visited:
                    visited.add(k)
                    q.append(k)
        return len(visited) == len(rooms)
