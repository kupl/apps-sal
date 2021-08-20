(t, s, x) = map(int, input().split())
x -= t
if x == 0 or (x >= s and (x % s == 0 or x % s == 1)):
    print('YES')
else:
    print('NO')
