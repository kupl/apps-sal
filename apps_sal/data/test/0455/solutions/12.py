from sys import stdin, exit
import numpy as np

N, *XY = map(int, stdin.read().split())
XY = np.array(XY).reshape(N, 2)

XYsum = np.abs(XY).sum(axis=1)
if any(XYsum % 2 != XYsum[0] % 2):
    print(-1)
    return

xymax = XYsum.max()
d = [] if xymax % 2 == 1 else [1]
for i in range(41):
    di = 2**i
    if xymax < di:
        break
    d.append(di)
d.reverse()
print(len(d))
print(' '.join(map(str, d)))

for X, Y in XY:
    x, y = 0, 0
    w = ''
    for di in d:
        if abs(X-(x-di)) + abs(Y-y) <= di:
            w += 'L'
            x -= di
        elif abs(X-(x+di)) + abs(Y-y) <= di:
            w += 'R'
            x += di
        elif abs(X-x) + abs(Y-(y-di)) <= di:
            w += 'D'
            y -= di
        else:
            w += 'U'
            y += di
    print(w)
