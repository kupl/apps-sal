n, m, k = list(map(int, input().split()))

if k < n:
    print(1 + k, 1)
else:
    k -= n

    a = k % (2 * (m - 1))
    b = k // (2 * (m - 1))

    if a < m - 1:  # low
        print(n - 2 * b, 2 + a)
    else:
        a -= (m - 1)
        print(n - 2 * b - 1, m - a)
