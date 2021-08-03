a, b, x = map(int, input().split())
if a > x:
    print('NO')
elif x - a < b:
    print('YES')
else:
    print('NO')
