a, b, c, d = list(map(int, input().split()))
m = list(range(2))
v = list(range(2))
m[0] = (a * 3) / 10
m[1] = a - (a / 250) * c
v[0] = (b * 3) / 10
v[1] = b - (b / 250) * d
mm = max(m)
vv = max(v)
if mm > vv:
    print('Misha')
elif mm < vv:
    print('Vasya')
else:
    print('Tie')
