n, w = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append(a[i] // 2 + a[i] % 2)
    w -= a[i] // 2 + a[i] % 2
if w < 0:
    print(-1)
else:
    while w > 0:
        m = a[0], 0
        for i in range(n):
            if a[i] > m[0]:
                m = [a[i], i]
        if w >= a[m[1]] - b[m[1]]:
            w -= a[m[1]] - b[m[1]]
            b[m[1]] = a[m[1]]
            a[m[1]] = 0
        else:
            b[m[1]] += w
            w = 0
    print(' '.join(map(str, b)))
