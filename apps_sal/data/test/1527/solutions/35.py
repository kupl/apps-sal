import queue
h,w = map(int,input().split())
v = [(1, 0), (0, 1), (-1, 0), (0, -1)]
s = [input() for i in range(h)]

ans = 0
que = queue.Queue()
for i in range(h * w):
    c = 0
    d = [[h*w] * w for i in range(h)]
    p = (i//w, i%w)
    if s[p[0]][p[1]] == '#':
        continue
    d[p[0]][p[1]] = 0
    que.put(p)
    while not que.empty():
        y,x = que.get()
        c = d[y][x]
        for dy, dx in v:
            yy = y + dy
            xx = x + dx
            if yy < 0 or xx < 0 or h <= yy or w <= xx:
                continue
            if s[yy][xx] == '#':
                continue
            if d[yy][xx] < h*w:
                continue
            que.put((yy, xx))
            d[yy][xx] = c + 1
    ans = max(ans, c)
print(ans)
