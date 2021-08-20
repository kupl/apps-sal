df = int(input())
for _ in range(df):
    (n, x, y, d) = list(map(int, input().split()))
    d2 = abs(x - y)
    ans = 3000000000.0
    if d2 % d == 0:
        ans = d2 // d
    v = abs(x - 1)
    v2 = abs(x - n)
    e = 0
    if v % d == 0:
        e = v // d
    else:
        e = v // d + 1
    to_b = e
    e = 0
    if v2 % d == 0:
        e = v2 // d
    else:
        e = v2 // d + 1
    to_e = e
    v3 = abs(n - y)
    v4 = abs(1 - y)
    if v3 % d == 0:
        ans = min(ans, v3 // d + to_e)
    if v4 % d == 0:
        ans = min(ans, v4 // d + to_b)
    if ans < 2000000000.0:
        print(ans)
    else:
        print(-1)
