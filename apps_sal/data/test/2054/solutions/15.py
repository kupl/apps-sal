for _ in range(int(input())):
    (n, m) = map(int, input().split())
    if m > n:
        (n, m) = (m, n)
    if n > 2 * m:
        n = 2 * m
    print((n + m) // 3)
