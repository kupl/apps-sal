a = [int(i) for i in input().split()]
a.sort()
if a[0] == 1:
    print('YES')
elif a[0] == 2 and a[1] == 2:
    print('YES')
elif a[0] == 2 and a[1] == 4 and a[2] == 4:
    print('YES')
elif a[0] == 3 and a[1] == 3 and a[2] == 3:
    print('YES')
else:
    print('NO')
