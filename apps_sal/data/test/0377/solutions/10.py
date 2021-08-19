(n, m) = list(map(int, input().split()))
if m <= n / 2:
    print(max(m, 1))
else:
    print(n - m)
