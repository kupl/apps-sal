(n, m) = [int(c) for c in input().split(' ')]
x = [int(c) for c in input().split(' ')]
y = [int(c) for c in input().split(' ')]
(ix, iy) = (0, 0)
(sumx, sumy) = (0, 0)
(xis, yis) = ([], [])
while True:
    if sumx == sumy:
        if sumx != 0:
            xis.append(ix - 1)
            yis.append(iy - 1)
            (sumx, sumy) = (0, 0)
        else:
            sumx += x[ix]
            sumy += y[iy]
            ix += 1
            iy += 1
    elif sumx > sumy:
        sumy += y[iy]
        iy += 1
    else:
        sumx += x[ix]
        ix += 1
    if ix == len(x) and iy == len(y):
        break
if len(xis) == len(yis):
    print(len(xis) + 1)
else:
    print('error', xis, yis)
