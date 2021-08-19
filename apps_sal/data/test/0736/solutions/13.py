(n, m) = map(int, input().split())
if n < m:
    print(-1)
else:
    x = n // 2 + n % 2
    while x % m != 0:
        x += 1
    print(x)
