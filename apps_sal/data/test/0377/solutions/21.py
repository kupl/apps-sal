(n, m) = list(map(int, input().split()))
if n == m:
    print(0)
elif m == 0:
    print(1)
elif n // 2 < m:
    print(n - m)
else:
    print(m)
