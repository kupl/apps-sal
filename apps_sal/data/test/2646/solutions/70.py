(n, m) = list(map(int, input().split()))
neighbors = {}
for _ in range(m):
    (a, b) = list(map(int, input().split()))
    if a not in list(neighbors.keys()):
        neighbors.update({a: set()})
    if b not in neighbors[a]:
        neighbors[a].add(b)
    if b not in list(neighbors.keys()):
        neighbors.update({b: set()})
    if a not in neighbors[b]:
        neighbors[b].add(a)
lst = [0] * (n - 1)
visited = set()
queue = [[0, set([1])]]
while queue:
    (pre_room, rooms) = queue.pop(0)
    for room in rooms:
        if room in visited:
            continue
        if lst[room - 2] == 0 and room != 1:
            lst[room - 2] = pre_room
        visited.add(room)
        next_rooms = set()
        for nei in neighbors[room]:
            next_rooms.add(nei)
        next_rooms = [room, next_rooms]
        queue.append(next_rooms)
if 0 in lst:
    print('No')
else:
    print('Yes')
    for i in range(n - 1):
        print(lst[i])
