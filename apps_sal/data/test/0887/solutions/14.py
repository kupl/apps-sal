n = int(input())
l = list(map(int, input().split()))
if n == 1:
    if l[0] == 1:
        print('YES')
    else:
        print('NO')
elif l.count(1) == n - 1:
    print('YES')
else:
    print('NO')
