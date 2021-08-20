(n, m, k) = map(int, input().split())
if k > n + m - 2:
    print(-1)
else:
    (a, b) = (m * (n // (k + 1)), n * (m // (k + 1)))
    if a == 0:
        a = m // (k - n + 2)
    if b == 0:
        b = n // (k - m + 2)
    print(max(a, b))
