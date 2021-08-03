n, W = map(int, input().split())
wv = [[]for _ in range(4)]
for i in range(n):
    w, v = map(int, input().split())
    if i == 0:
        r = w
        wv[0].append(v)
    else:
        wv[w - r].append(v)
for i in range(4):
    wv[i].sort(reverse=True)
    for j in range(len(wv[i]) - 1):
        wv[i][j + 1] += wv[i][j]
    wv[i].insert(0, 0)
ans = 0
for i in range(len(wv[0])):
    for j in range(len(wv[1])):
        for k in range(len(wv[2])):
            for l in range(len(wv[3])):
                p = wv[0][i] + wv[1][j] + wv[2][k] + wv[3][l]
                if i * r + j * (r + 1) + k * (r + 2) + l * (r + 3) <= W:
                    ans = max(ans, p)
print(ans)
