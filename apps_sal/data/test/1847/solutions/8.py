# ip = open("testdata.txt", "r")

# def input():
# 	return ip.readline().strip()

from collections import deque, defaultdict

x0, y0, x1, y1 = map(int, input().split())

allowed = defaultdict(list)
allowed[x0].append([y0, y0])
allowed[x1].append([y1, y1])

m = int(input())

for _ in range(m):
    r, a, b = map(int, input().split())
    allowed[r].append([a, b])


def get_valid_moves(x, y):
    valid_pos = set()
    if x in allowed:
        for l, r in allowed[x]:
            if l <= y - 1 <= r:
                valid_pos.add((x, y - 1))
            if l <= y + 1 <= r:
                valid_pos.add((x, y + 1))
    if x - 1 in allowed:
        for l, r in allowed[x - 1]:
            if l <= y - 1 <= r:
                valid_pos.add((x - 1, y - 1))
            if l <= y <= r:
                valid_pos.add((x - 1, y))
            if l <= y + 1 <= r:
                valid_pos.add((x - 1, y + 1))
    if x + 1 in allowed:
        for l, r in allowed[x + 1]:
            if l <= y - 1 <= r:
                valid_pos.add((x + 1, y - 1))
            if l <= y <= r:
                valid_pos.add((x + 1, y))
            if l <= y + 1 <= r:
                valid_pos.add((x + 1, y + 1))
    return valid_pos


def bfs():
    nonlocal x0, y0, x1, y1
    dq = deque([(x0, y0)])
    vis_set = {(x0, y0), }
    level = defaultdict(int)
    while dq:
        x0, y0 = dq.popleft()
        for x, y in get_valid_moves(x0, y0):
            if not (x, y) in vis_set:
                level[(x, y)] = level[(x0, y0)] + 1
                if (x, y) == (x1, y1):
                    return level[(x, y)]
                vis_set.add((x, y))
                dq.append((x, y))
    return -1


ans = bfs()
print(ans)
