(n, m) = map(int, input().split())
py = [list(map(int, input().split())) for i in range(m)]
ipy = [[0, 0, 0]]
for i in range(m):
    ipy.append([i] + py[i])
ipy = sorted(ipy, key=lambda x: (x[1], x[2]))
for i in range(1, m + 1):
    if ipy[i][1] != ipy[i - 1][1]:
        cnt = 0
    cnt += 1
    ipy[i].append(str(ipy[i][1]).zfill(6) + str(cnt).zfill(6))
ipy = sorted(ipy)
for i in range(1, m + 1):
    print(ipy[i][3])
