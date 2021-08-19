n = int(input())
txylist = [[0, 0, 0]]
for i in range(n):
    txy = list(map(int, input().split(' ')))
    txylist += [txy]
for i in range(n):
    p = False
    (t0, x0, y0) = txylist[i]
    (t1, x1, y1) = txylist[i + 1]
    (t, x, y) = (t1 - t0, x1 - x0, y1 - y0)
    tt = abs(x) + abs(y)
    legs = t - tt
    if legs >= 0 and legs % 2 == 0:
        p = True
    else:
        print('No')
        break
if p == True:
    print('Yes')
