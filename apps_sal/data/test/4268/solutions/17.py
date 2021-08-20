(n, d) = map(int, input().split())
point = []
for _ in range(n):
    point.append(list(map(int, input().split())))
ans = 0
for i in range(n - 1):
    for l in range(i, n):
        if i == l:
            continue
        dis = 0
        for f in range(d):
            dis += (point[i][f] - point[l][f]) ** 2
        dis = dis ** 0.5
        if dis.is_integer():
            ans += 1
print(ans)
