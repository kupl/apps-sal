class GraphNode:

    def __init__(self):
        self.neighbors = set()


class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        nodes = [GraphNode() for i in range(len(rooms))]
        for (index, keys) in enumerate(rooms):
            for key in keys:
                nodes[index].neighbors.add(nodes[key])
        stack = [nodes[0]]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for neighbor in node.neighbors:
                stack.append(neighbor)
        return len(visited) == len(rooms)
