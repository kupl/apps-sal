n = int(input())
xyd = [list(input().split()) for i in range(n)]
(xmax, ymax) = ([-10 ** 9, -10 ** 9, -10 ** 9], [-10 ** 9, -10 ** 9, -10 ** 9])
(xmin, ymin) = ([10 ** 9, 10 ** 9, 10 ** 9], [10 ** 9, 10 ** 9, 10 ** 9])


def chp(ls, a, flg1, i):
    if flg1:
        ls[i] = max(ls[i], a)
    else:
        ls[i] = min(ls[i], a)


def area(t):
    x = max(xmax[0] - t, xmax[1], xmax[2] + t) - min(xmin[0] + t, xmin[1], xmin[2] - t)
    y = max(ymax[0] - t, ymax[1], ymax[2] + t) - min(ymin[0] + t, ymin[1], ymin[2] - t)
    return x * y


for (x, y, d) in xyd:
    (x, y) = (int(x), int(y))
    if d in ('L', 'R'):
        chp(ymax, y, 1, 1)
        chp(ymin, y, 0, 1)
        if d == 'R':
            chp(xmin, x, 0, 0)
            chp(xmax, x, 1, 2)
        if d == 'L':
            chp(xmin, x, 0, 2)
            chp(xmax, x, 1, 0)
    elif d in ('U', 'D'):
        chp(xmax, x, 1, 1)
        chp(xmin, x, 0, 1)
        if d == 'U':
            chp(ymax, y, 1, 2)
            chp(ymin, y, 0, 0)
        if d == 'D':
            chp(ymin, y, 0, 2)
            chp(ymax, y, 1, 0)
event = [0]
for ls in (xmax, ymax):
    event.append(ls[0] - ls[1])
    event.append((ls[0] - ls[2]) / 2)
    event.append(ls[1] - ls[2])
for ls in (xmin, ymin):
    event.append(ls[1] - ls[0])
    event.append((ls[2] - ls[0]) / 2)
    event.append(ls[2] - ls[1])
ans = 10 ** 18
for i in event:
    if i >= 0:
        for j in range(-10, 10):
            if i + j * 0.5 >= 0:
                ans = min(ans, area(i + j * 0.5))
print(ans)
