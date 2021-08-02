n, w = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [(x + 1) // 2 for x in a]
w -= sum(b)
if w > 0:
    a = [(a[i], i) for i in range(n)]
    a.sort(reverse=True)
    for i in range(n):
        x = min(a[i][0] - b[a[i][1]], w)
        w -= x
        b[a[i][1]] += x
        if w == 0:
            break
if w >= 0:
    print(*b)
else:
    print(-1)
