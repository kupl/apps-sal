a = list(map(int, input().split()))
a.sort()
if a[0] + a[3] == a[1] + a[2] or sum(a[:3]) == a[3]:
    print('YES')
else:
    print('NO')
