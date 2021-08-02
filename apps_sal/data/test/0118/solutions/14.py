__author__ = 'Utena'
t, s, x = map(int, input().split())
if x >= t:
    if not x - t == 1:
        if (x - t) % s == 0 or (x - t - 1) % s == 0:
            print('YES')
            return
    else:
        if (x - t) % s == 0:
            print('YES')
            return
print('NO')
