n = int(input())
a = list(map(int, input().split()))
if len(a) == 1:
    if a[0] == 1:
        print('YES')
    else:
        print('NO')
else:
    zeros = a.count(0)
    if zeros == 1:
        print('YES')
    else:
        print('NO')
