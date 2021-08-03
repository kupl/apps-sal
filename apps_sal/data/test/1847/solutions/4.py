from collections import defaultdict

x0, y0, x1, y1 = [int(c) for c in input().split()]
n = int(input())

allowed = defaultdict(set)
for _ in range(n):
    row, col_x, col_y = [int(c) for c in input().split()]
    for c in range(col_x, col_y + 1):
        allowed[row].add(c)

start, end = (x0, y0), (x1, y1)
if start == end:
    print(0)
    return

queue = [start]
visited = {start}

neighbors = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if not (i == 0 and j == 0):
            neighbors.append((i, j))

ans = 1
while queue:
    new_queue = []
    for pos in queue:
        for neigh in neighbors:
            cur = pos[0] + neigh[0], pos[1] + neigh[1]
            if cur == end:
                print(ans)
                return
            if 1 <= cur[0] <= 10**9 and 1 <= cur[1] <= 10**9:
                if cur[0] in allowed and cur[1] in allowed[cur[0]]:
                    if cur not in visited:
                        visited.add(cur)
                        new_queue.append(cur)

    ans += 1
    queue = new_queue

print(-1)
