n, m = list(map(int, input().split()))
if m == 0:
    print(1)
elif m <= n // 2:
    print(m)
else:
    print(n - m)
