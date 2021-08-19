(t, s, x) = list(map(int, input().split()))
k1 = (x - t) // s
k2 = (x - t - 1) // s
if k1 >= 0 and t + k1 * s == x or (k2 > 0 and t + k2 * s + 1 == x):
    print('YES')
else:
    print('NO')
