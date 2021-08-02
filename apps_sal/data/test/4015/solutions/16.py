n, m = list(map(int, input().split()))
res, d = -1, 0
if m % n == 0:
    res = 0
    d = m // n
    while d % 2 == 0:
        d, res = d // 2, res + 1
    while d % 3 == 0:
        d, res = d // 3, res + 1
if d == 1:
    print(res)
else:
    print(-1)
