n, a, b, c = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(int(input()))
ans = 100000
for i in range(4**n):
    mp = 0
    f = 0
    x = []
    y = []
    z = []
    w = []
    for j in range(n):
        if i % 4 == 0:
            x.append(l[j])
        elif i % 4 == 1:
            y.append(l[j])
        elif i % 4 == 2:
            z.append(l[j])
        else:
            w.append(l[j])
        i = i // 4
    if sum(x) == 0 or sum(y) == 0 or sum(z) == 0:
        f = 1

    X = sum(x)
    Y = sum(y)
    Z = sum(z)
    mp += (len(x) + len(y) + len(z) - 3) * 10
    p = [X, Y, Z]
    q = [a, b, c]
    p = sorted(p)
    q = sorted(q)
    mp += abs(p[0] - q[0]) + abs(p[1] - q[1]) + abs(p[2] - q[2])
    if f != 1:
        ans = (min(mp, ans))
print(ans)
