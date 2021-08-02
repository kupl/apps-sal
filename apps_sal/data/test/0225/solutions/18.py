a = [int(x) for x in input().split()]
a.sort()
if sum(a) % 2 == 0:
    counter = sum(a) // 2
    if a[0] + a[1] == counter or a[1] + a[2] == counter or a[0] + a[2] == counter or a[0] == counter or a[1] == counter or a[2] == counter or a[3] == counter:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
