(n, m, k, l) = map(int, input().split())
mm = k + l
if mm % m == 0:
    mm //= m
else:
    mm = mm // m + 1
if n < mm * m:
    print(-1)
else:
    print(mm)
