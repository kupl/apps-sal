import sys

K = int(input())
X, Y = list(map(int, input().split()))

mx = 1 if X >= 0 else -1
my = 1 if Y >= 0 else -1
X, Y = abs(X), abs(Y)
isSwaped = False
if X < Y:
    X, Y = Y, X
    isSwaped = True

dist = X + Y
if dist % K == 0:
    rx, ry = 0, 0
else:
    if dist % 2 == 0:
        if K % 2 == 0:
            if dist <= 2 * K:
                R = 2 * K
            else:
                R = -(-dist // K) * K
        else:
            R = -(-dist // (2 * K)) * 2 * K
    else:
        if K % 2 == 0:
            print((-1))
            return
        else:
            if dist <= 3 * K:
                R = 3 * K
            else:
                R = -(-(dist - K) // (2 * K)) * 2 * K + K
    r = (R - dist) // 2

    if r < K:
        rx, ry = 0, r
    else:
        rx = r // 2
        ry = r - rx

anss = []
x, y = 0, 0
if -ry < y:
    dy = y + ry
    y -= dy
    x += K - dy
    anss.append((x, y))

num = (X + rx - x) // K
for _ in range(num):
    x += K
    anss.append((x, y))

if x < X + rx:
    dx = X + rx - x
    x += dx
    y += K - dx
    anss.append((x, y))

num = (Y - y) // K
for _ in range(num):
    y += K
    anss.append((x, y))

if y < Y:
    dy = Y - y
    y += dy
    x -= K - dy
    anss.append((x, y))

print((len(anss)))
if isSwaped:
    print(('\n'.join([str(x[1] * mx) + ' ' + str(x[0] * my) for x in anss])))
else:
    print(('\n'.join([str(x[0] * mx) + ' ' + str(x[1] * my) for x in anss])))
