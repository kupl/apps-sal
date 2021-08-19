N = int(input())
sxy41 = []
sxy23 = []
for i in range(N):
    (x, y) = list(map(int, input().split()))
    if x == 0 and y >= 0:
        s = float('inf')
    elif x == 0 and y < 0:
        s = -1 * float('inf')
    else:
        s = y / x
    if x >= 0:
        sxy41.append([s, x, y])
    else:
        sxy23.append([s, x, y])
sxy41.sort()
sxy23.sort()
sxy = []
for i in sxy41:
    sxy.append(i)
for i in sxy23:
    sxy.append(i)
ans = 0
for i in range(N):
    for j in range(i):
        nowx = 0
        nowy = 0
        for k in range(i - j + 1):
            k += j
            nowx += sxy[k][1]
            nowy += sxy[k][2]
        ans = max(ans, (nowx ** 2 + nowy ** 2) ** 0.5)
sxy = []
for i in sxy23:
    sxy.append(i)
for i in sxy41:
    sxy.append(i)
for i in range(N):
    for j in range(i + 1):
        nowx = 0
        nowy = 0
        for k in range(i - j + 1):
            k += j
            nowx += sxy[k][1]
            nowy += sxy[k][2]
        ans = max(ans, (nowx ** 2 + nowy ** 2) ** 0.5)
print(ans)
