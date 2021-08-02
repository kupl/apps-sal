
h, w = list(map(int, input().split()))
s = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            continue
        ok = False
        for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            nx = j + dx
            ny = i + dy
            if 0 <= nx < w and 0 <= ny < h and s[ny][nx] == '#':
                ok = True
        if not ok:
            print('No')
            return
print('Yes')
