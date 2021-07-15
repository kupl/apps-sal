R, C = list(map(int, input().split()))
line = '.' * (C+2)
wall = [line]
for _ in range(R):
    wall.append('.' + input() + '.')
wall.append(line)

vs = set()
ans = 0


def visit(r, c):
    q = [(r, c)]
    while q:
        r, c = q.pop()
        if (r, c) in vs:
            continue
        vs.add((r, c))
        if wall[r-1][c] == 'B':
            q.append((r-1, c))
        if wall[r+1][c] == 'B':
            q.append((r+1, c))
        if wall[r][c-1] == 'B':
            q.append((r, c-1))
        if wall[r][c+1] == 'B':
            q.append((r, c+1))

for r in range(1, R+1):
    for c in range(1, C+1):
        if wall[r][c] == 'B' and (r, c) not in vs:
            ans += 1
            visit(r, c)

print(ans)

