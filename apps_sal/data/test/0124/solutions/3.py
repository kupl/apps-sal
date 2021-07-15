x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

f = a
s = a + b
t = a + c + b

f -= x
s = s - x - y
t = t - x - y - z

if f < 0 or s < 0 or t < 0:
    print('NO')
else:
    print('YES')
