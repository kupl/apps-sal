def f():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    for i in range(m - 1):
        if a[i] + 1 == a[i + 1]:
            return 0
    mod = 10**9 + 7
    x = [1] * (n + 1)
    for j in a:
        x[j] = 0
    for k in range(2, n + 1):
        if x[k] == 1:
            x[k] = (x[k - 1] + x[k - 2]) % mod
    return x[n]


print(f())
