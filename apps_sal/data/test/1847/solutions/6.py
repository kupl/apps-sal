from collections import deque

x_start, y_start, x_end, y_end = [int(x) for x in input().split()]
n = int(input())
moves = {}
for _ in range(n):
    r, a, b = [int(x) for x in input().split()]
    for j in range(a, b + 1):
        moves[(r, j)] = -1

p_start = x_start, y_start
d = deque([p_start])
moves[p_start] = 0
while d:
    x1, y1 = d.popleft()
    m = moves[(x1, y1)]
    for p2 in [(x1 + dx, y1 + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]:
        if (p2 in moves) and (moves[p2] == -1):
            d.append(p2)
            moves[p2] = m + 1

print(moves[(x_end, y_end)])
