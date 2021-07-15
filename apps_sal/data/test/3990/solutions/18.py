def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return len(new_path)-1
            explored.append(node)
    return -1


town_rail = input().split(" ")
town = int(town_rail[0])
rail = int(town_rail[1])
railways = []
graph = {}
for j in range(1,town+1):
    graph[j] = []

for i in range(rail):
    railways.append(input().split(" "))

if ["1", str(town)] in railways or [str(town),"1"] in railways:
    for key in graph:
        for k in range(1,town+1):
            if k != key:
                graph[key].append(k)
    for pair in railways:
        graph[int(pair[0])].remove(int(pair[1]))
        graph[int(pair[1])].remove(int(pair[0]))
else:
    for pair in railways:
        graph[int(pair[0])].append(int(pair[1]))
        graph[int(pair[1])].append(int(pair[0]))
print(bfs_shortest_path(graph, 1, town))
