x, k, d = map(int, input().split())

if x < 0:
    x *= -1

m = x // d

if k <= m:
    print(x - k * d)

else:
    x %= d
    y = abs(x - d)

    print([x, y][(k - m) % 2])
