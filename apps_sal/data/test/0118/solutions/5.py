(t, s, x) = map(int, input().split())
if x < t:
    print('NO')
elif x == t + 1 and s != 1:
    print('NO')
elif (x - t) % s == 0 or (x - t - 1) % s == 0:
    print('YES')
else:
    print('NO')
