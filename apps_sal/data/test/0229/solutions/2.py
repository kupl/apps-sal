n = int(input())
a = sorted(list(set(list(map(int, input().split())))))
if len((a)) < 3:
    print('YES')
elif len((a)) > 3:
    print('NO')
else:
    if a[1] - a[0] == a[2] - a[1]:
        print('YES')
    else:
        print('NO')
