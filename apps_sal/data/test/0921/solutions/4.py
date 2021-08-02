n, w = map(int, input().split())
a = list(map(int, input().split()))
s = 0
for i in range(n):
    s += (a[i] + 1) // 2
    a[i] = [a[i], i]
if s > w:
    print(-1)
else:
    res = [[(a[i][0] + 1) // 2, i] for i in range(n)]
    w -= s
    a.sort(reverse=True)
    i = 0
    while w > 0:
        res[a[i][1]][0] = min(a[i][0], res[a[i][1]][0] + w)
        w -= a[i][0] // 2
        i += 1
    for i in range(n):
        print(res[i][0], end=' ')
