(n, m) = [int(x) for x in input().split()]
(k, t) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
if a[k - 1] < b[m - t]:
    print('YES')
else:
    print('NO')
