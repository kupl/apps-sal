I = float('inf')
N = int(input())
XYD = [input().split() for _ in range(N)]
xL = set()
xR = set()
xS = set()
yD = set()
yU = set()
yS = set()
for xyd in XYD:
    x, y, d = xyd
    x = int(x)
    y = int(y)
    if d == 'L':
        xL.add(x)
        yS.add(y)
    elif d == 'R':
        xR.add(x)
        yS.add(y)
    elif d == 'U':
        yU.add(y)
        xS.add(x)
    else:
        yD.add(y)
        xS.add(x)
#xmin
xRmin = min(xR | {I})
xLmin = min(xL | {I})
xSmin = min(xS | {I})
#xmax
xRmax = max(xR | {-I})
xLmax = max(xL | {-I})
xSmax = max(xS | {-I})

x2m = xLmax - xRmin
x1m = max(xSmax - xRmin, xLmax - xSmin)
x0 = max(xRmax - xRmin, xLmax - xLmin, xSmax - xSmin)
x1 = max(xSmax - xLmin, xRmax - xSmin)
x2 = xRmax - xLmin
#ymin
yUmin = min(yU | {I})
yDmin = min(yD | {I})
ySmin = min(yS | {I})
#ymax
yUmax = max(yU | {-I})
yDmax = max(yD | {-I})
ySmax = max(yS | {-I})

y2m = yDmax - yUmin
y1m = max(ySmax - yUmin, yDmax - ySmin)
y0 = max(yUmax - yUmin, yDmax - yDmin, ySmax - ySmin)
y1 = max(ySmax - yDmin, yUmax - ySmin)
y2 = yUmax - yDmin


def dd(t):
    if 0 <= t < I:
        return max(x2m - 2 * t, x1m - t, x0, x1 + t, x2 + 2 * t) * max(
            y2m - 2 * t, y1m - t, y0, y1 + t, y2 + 2 * t)
    else:
        return I


t = [0, x2m / 2, x1m, y2m / 2, y1m]
t += [x2m - x1m, x1m - x0, x0 - x1, x1 - x2]
t += [(x2m - x0) / 2, (x1m - x1) / 2, (x0 - x2) / 2]
t += [(x2m - x1) / 3, (x1m - x2) / 3]
t += [(x2m - x2) / 4]
t += [y2m - y1m, y1m - y0, y0 - y1, y1 - y2]
t += [(y2m - y0) / 2, (y1m - y1) / 2, (y0 - y2) / 2]
t += [(y2m - y1) / 3, (y1m - y2) / 3]
t += [(y2m - y2) / 4]
t += [(x2m + y2m) / 4, (x2 + y2) / 4]
t += [(x2m + 2 * y1m) / 4, (y1m + 2 * x2m) / 4, (x2 + 2 * y1) / 4,
      (y1 + 2 * x2) / 4]
t += [(x1m + y1m) / 2, (x1 + y1) / 2]

print((min([dd(time) for time in t])))

