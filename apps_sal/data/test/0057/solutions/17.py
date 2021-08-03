n = int(input())
x, y = [], []
for i in range(n):
    _x, _y = list(map(int, input().split()))
    x.append(_x)
    y.append(_y)
x = sorted(set(x))
y = sorted(set(y))
if len(x) == 2 and len(y) == 2:
    print((x[1] - x[0]) * (y[1] - y[0]))
else:
    print(-1)
