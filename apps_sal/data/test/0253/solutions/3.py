k, m, n = list(map(int, input().split()))
mn = min(k, min(m, n))
ma = max(k, max(m, n))
me = k + m + n - mn - ma
if mn == 1 or (mn == me == 2) or (mn == 2 and me == ma == 4) or mn == ma == me == 3:
    print('YES')
else:
    print('NO')
