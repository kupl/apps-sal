n = int(input())
xs = set()
ys = set()
for i in range(n):
    x, y = map(int, input().split())
    xs.add(x)
    ys.add(y)
if len(xs) == 2 and len(ys) == 2:
    x1, x2 = xs
    y1, y2 = ys
    print(abs((x1 - x2)*(y1 - y2)))
else:
    print(-1)
