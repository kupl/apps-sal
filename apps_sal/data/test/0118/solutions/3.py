(t, s, x) = list(map(int, input().split()))
x -= t
if (x % s == 0 or x % s == 1) and x >= s or x == 0:
    print('YES')
else:
    print('NO')
