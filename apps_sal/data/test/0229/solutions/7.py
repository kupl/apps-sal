n = int(input())
a = set(map(int, input().split()))
if len(a) > 3:
    print('NO')
elif len(a) < 3:
    print('YES')
else:
    a = list(a)
    a.sort()
    if (a[0] + a[2]) / 2 == a[1]:
        print('YES')
    else:
        print('NO')
