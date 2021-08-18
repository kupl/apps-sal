H, W = map(int, input().split())
field = []
for h in range(H):
    field.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 'Yes'
for h in range(H):
    for w in range(W):
        if field[h][w] != '
        continue
        ok = False
        for i in range(4):
            nw = dx[i] + w
            nh = dy[i] + h
            if nw < 0 or W <= nw or nh < 0 or H <= nh:
                continue
            if field[nh][nw] == '
            ok = True
        if not ok:
            ans = 'No'

print(ans)
