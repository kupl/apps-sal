from bisect import insort_left as bs
b = []
a = []
n, k = list(map(int, input().split()))
for i in range(n):
    x, y = list(map(int, input().split()))
    a.append([x, y, i + 1])
    b.append([x, y, i + 1])
a.sort()
ans = [[a[0][1], a[0][2]]]
le = 1
vis = [0] * 201
printans = []
for i in a:
    x, y, ind = i[0], i[1], i[2]
    if i != a[0]:
        bs(ans, [y, ind], 0, le)
        le += 1
    for j in range(x, y + 1):
        if vis[j] >= k:
            p, q = ans.pop()
            le -= 1
            for l in range(b[q - 1][0], p + 1):
                vis[l] -= 1
            printans.append(q)
            for l in range(x, y + 1):
                vis[l] += 1
            break
    else:
        for j in range(x, y + 1):
            vis[j] += 1


print(len(printans))
print(*printans)
