
xx = set()
yy = set()
l = set()
for i in range(8):
    a = list(map(int, input().split()))
    x, y = a[0], a[1]
    l.add((x, y))
    xx.add(x)
    yy.add(y)

ok = 1
if (len(xx) != 3) or (len(yy) != 3) or (len(l) != 8):
    ok = 0
else:
    ax = list(xx)
    ay = list(yy)
    ax.sort()
    ay.sort()
    if (ax[1], ay[1]) in l:
        ok = 0


if ok == 1:
    print('respectable')
else:
    print('ugly')
