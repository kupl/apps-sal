n = int(input())
a = sum(map(int, input().split(' ')))
if n == 1:
    if a == 1:
        print('YES')
    else:
        print('NO')
elif a == n - 1:
    print('YES')
else:
    print('NO')
