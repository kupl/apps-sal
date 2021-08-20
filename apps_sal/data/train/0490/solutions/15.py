class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                graph[i].append(rooms[i][j])
        visited = set()
        q = [0]
        while q:
            item = q.pop(0)
            if item not in visited:
                visited.add(item)
                for val in graph[item]:
                    q.append(val)
        if len(visited) == len(rooms):
            return True
        else:
            return False
