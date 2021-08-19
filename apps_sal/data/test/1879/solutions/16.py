(t, sx, sy, ex, ey) = map(int, input().split())
w = input()
n = len(w)
w += ' '
ans = -1
i = 0
dx = ex - sx
dy = ey - sy
if abs(dx) + abs(dy) > t:
    pass
else:
    while i <= t and i < n:
        if dx == 0 and dy == 0:
            ans = i
            break
        if dx >= 0 and dy >= 0:
            if (w[i] != 'E' and w[i] != 'N' or (dx == 0 and w[i] == 'E') or (dy == 0 and w[i] == 'N')) and i < n:
                i += 1
            if dx > 0 and w[i] == 'E' and (i < n):
                i += 1
                dx -= 1
            if dy > 0 and w[i] == 'N' and (i < n):
                i += 1
                dy -= 1
        elif dx >= 0 and dy <= 0:
            if (w[i] != 'E' and w[i] != 'S' or (dx == 0 and w[i] == 'E') or (dy == 0 and w[i] == 'S')) and i < n:
                i += 1
            if dx > 0 and w[i] == 'E' and (i < n):
                i += 1
                dx -= 1
            if dy < 0 and w[i] == 'S' and (i < n):
                i += 1
                dy += 1
        elif dx <= 0 and dy >= 0:
            if (w[i] != 'W' and w[i] != 'N' or (dx == 0 and w[i] == 'W') or (dy == 0 and w[i] == 'N')) and i < n:
                i += 1
            if dx < 0 and w[i] == 'W' and (i < n):
                i += 1
                dx += 1
            if dy > 0 and w[i] == 'N' and (i < n):
                i += 1
                dy -= 1
        elif dx <= 0 and dy <= 0:
            if (w[i] != 'W' and w[i] != 'S' or (dx == 0 and w[i] == 'W') or (dy == 0 and w[i] == 'S')) and i < n:
                i += 1
            if dx < 0 and w[i] == 'W' and (i < n):
                i += 1
                dx += 1
            if dy < 0 and w[i] == 'S' and (i < n):
                i += 1
                dy += 1
if dx == 0 and dy == 0:
    ans = i
print(ans)
