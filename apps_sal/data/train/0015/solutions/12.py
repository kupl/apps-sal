for _ in range(int(input())):
    (n, m, x, y) = map(int, input().split())
    s = 0
    s = max(s, x * m)
    s = max(s, (n - x - 1) * m)
    s = max(s, y * n)
    s = max(s, (m - y - 1) * n)
    print(s)
