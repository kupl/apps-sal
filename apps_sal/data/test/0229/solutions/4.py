input()
a = list(map(int, input().split()))
a = sorted(set(a))
if len(a) >= 4:
    print('NO')
elif len(a) <= 2:
    print('YES')
elif a[1] - a[0] == a[2] - a[1]:
    print('YES')
else:
    print('NO')
