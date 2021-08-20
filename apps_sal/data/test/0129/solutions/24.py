(n, m, k, l) = list(map(int, input().split()))
x = -(-(k + l) // m)
if x <= n / m:
    print(x)
else:
    print(-1)
