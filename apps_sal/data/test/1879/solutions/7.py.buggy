d = {'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), 'N': (0, 1)}
t, sx, sy, ex, ey = [int(x) for x in input().split()]
s = input()
for i in range(t):
    c = s[i]
    dx, dy = d[c]
    if abs(sx + dx - ex) <= abs(sx - ex) and abs(sy + dy - ey) <= abs(sy - ey):
        sx += dx
        sy += dy
    if sx == ex and sy == ey:
        print(i + 1)
        return
print(-1)
