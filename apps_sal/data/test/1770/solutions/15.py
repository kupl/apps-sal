t = int(input())
for i in range(t):
    (n, x, y, d) = list(map(int, input().split()))
    x -= 1
    y -= 1
    n -= 1
    a = abs(x - y)
    if a % d == 0:
        print(a // d)
        continue
    if y % d != 0 and (n - y) % d != 0:
        print(-1)
        continue
    i1 = max(0, (n - x + d - 1) // d) + (n - y) // d
    if (n - y) % d != 0:
        i1 = 10000000000.0
    i2 = max(0, (x + d - 1) // d) + y // d
    if y % d != 0:
        i2 = 10000000000.0
    print(min(i1, i2))
