(t, x, y, u, v) = map(int, input().split())
dx = u - x
dy = v - y
p = input()
(e, s, w, n) = (p.count('E'), p.count('S'), p.count('W'), p.count('N'))
if -w > dx or e < dx or -s > dy or (n < dy):
    print(-1)
else:
    for i in range(len(p)):
        if p[i] == 'E':
            if dx > 0:
                dx -= 1
        elif p[i] == 'S':
            if dy < 0:
                dy += 1
        elif p[i] == 'W':
            if dx < 0:
                dx += 1
        elif dy > 0:
            dy -= 1
        if dx == 0 and dy == 0:
            print(i + 1)
            break
