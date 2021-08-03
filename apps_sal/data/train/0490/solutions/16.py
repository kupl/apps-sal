class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                graph[i].append(rooms[i][j])

        visited = set()
        item = 0

        def rec(item):
            if item not in visited:
                visited.add(item)
                for val in graph[item]:
                    rec(val)
        rec(item)

        if len(visited) == len(rooms):
            return True
        else:
            return False
