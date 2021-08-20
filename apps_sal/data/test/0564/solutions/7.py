(n, m) = map(int, input().split())
a = sorted(list(map(int, input().split())))
if sum(a[:-1]) <= m:
    print('YES')
else:
    print('NO')
