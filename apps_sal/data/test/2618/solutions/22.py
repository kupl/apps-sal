def nod(a, b):
    while a * b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def rec(m, x, a, y, b):
    nonlocal p
    cx, cy, cxy = 0, 0, 0
    for i in range(1, m + 1):
        if i % a == 0 and i % b == 0:
            cxy += 1
        elif i % a == 0:
            cx += 1
        elif i % b == 0:
            cy += 1
    ans = 0

    for i in range(cxy):
        ans += p[i] * (x + y)
    for i in range(cx):
        ans += p[cxy + i] * x
    for i in range(cy):
        ans += p[cxy + cx + i] * y

    return ans


n = int(input())
for i in range(n):
    q = int(input())
    p = [int(j) for j in input().split()]
    p.sort(reverse=True)
    x, a = list(map(int, input().split()))
    y, b = list(map(int, input().split()))
    if y > x:
        x, a, y, b = y, b, x, a
    k = int(input())
    k = k * 100
    lf = 0
    rg = q + 1
    while rg - lf > 1:
        m = (rg + lf) // 2
        if rec(m, x, a, y, b) >= k:
            rg = m
        else:
            lf = m
    if rg > q:
        rg = -1
    print(rg)
