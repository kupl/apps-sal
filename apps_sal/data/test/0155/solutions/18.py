(n, m, k) = list(map(int, input().split()))

if k <= n - 1:
    print(1 + k, 1)
else:
    k -= n
    d = k // (m - 1)
    k %= (m - 1)
    if d % 2 == 0:
        print(n - d, k + 2)
    else:
        print(n - d, m - k)
