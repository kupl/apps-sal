
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    x = min(m, n // k)
    m -= x
    y = (m + (k - 1) - 1) // (k - 1)
    print(x - y)
