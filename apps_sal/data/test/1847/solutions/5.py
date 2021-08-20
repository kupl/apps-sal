from collections import deque
(px1, py1, px2, py2) = [int(x) for x in input().split()]
(p_start, p_end) = ((px1, py1), (px2, py2))
n = int(input())
valid = set()
for _ in range(n):
    (r, a, b) = [int(x) for x in input().split()]
    valid.update(((r, j) for j in range(a, b + 1)))
d = deque()
d.append((p_start, 0))
visited = {p_start}
while d:
    (p1, m) = d.popleft()
    if p1 == p_end:
        print(m)
        quit()
    for p2 in [(p1[0] + dx, p1[1] + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]:
        if p2 in valid and p2 not in visited:
            visited.add(p2)
            d.append((p2, m + 1))
print(-1)
