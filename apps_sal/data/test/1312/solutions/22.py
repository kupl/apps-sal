n, m = map(int, input().split())
for i in range(m):
    print(n // m, end=' ')
    n -= n // m
    m -= 1
