Len = list(map(int, input().split()))

if Len.count(5) == 2 and Len.count(7) == 1:
    print('YES')
else:
    print('NO')
