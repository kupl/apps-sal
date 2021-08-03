t, s, x = list(map(int, input().split(' ')))
if x == t or x >= t + s and ((x - t) % s == 0 or (x - t - 1) % s == 0):
    print('YES')
else:
    print('NO')
