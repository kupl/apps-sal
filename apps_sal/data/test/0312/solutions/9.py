(n, m) = list(map(int, input().split()))
if m == 1 and n == 1:
    print(1)
elif m == 1:
    print(2)
elif m == n:
    print(n - 1)
elif m - 1 < n - m:
    print(m + 1)
else:
    print(m - 1)
