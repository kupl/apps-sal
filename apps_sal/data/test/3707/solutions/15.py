(n, t, k, d) = map(int, input().split())
whenD = d // t * k
if n - whenD <= k:
    print('NO')
else:
    print('YES')
