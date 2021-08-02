x, y, z, t1, t2, t3 = map(int, input().split())

a1 = abs(x - y) * t1
a2 = abs(x - y) * t2 + 3 * t3
if z != x:
    a2 += abs(x - z) * t2
if a2 <= a1:
    print('YES')
else:
    print('NO')
