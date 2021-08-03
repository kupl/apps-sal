import itertools
N = int(input())
XY = [[int(_) for _ in input().split()] for _ in range(N)]
xy1 = []
xy2 = []
xy3 = []
xy4 = []
for x, y in XY:
    if x >= 0:
        if y >= 0:
            xy1 += [[x, y]]
        else:
            xy4 += [[x, y]]
    else:
        if y >= 0:
            xy2 += [[x, y]]
        else:
            xy3 += [[x, y]]
xy1.sort(key=lambda xy: float('inf') if xy[0] == 0 else xy[1] / xy[0])
xy2.sort(key=lambda xy: xy[1] / xy[0])
xy3.sort(key=lambda xy: xy[1] / xy[0])
xy4.sort(key=lambda xy: -float('inf') if xy[0] == 0 else xy[1] / xy[0])
XY = xy1 + xy2 + xy3 + xy4
N = len(XY)
XY *= 2
acc = list(
    itertools.accumulate(XY, func=lambda a, b: [a[0] + b[0], a[1] + b[1]]))
ans = 0
for i in range(N):
    for j in range(i + 1, i + N + 1):
        x = acc[j][0] - acc[i][0]
        y = acc[j][1] - acc[i][1]
        ans = max(ans, x**2 + y**2)
print((ans**0.5))
