ss = input().split('T')
(x, y) = list(map(int, input().split()))
dpx = dict()
dpy = dict()
dpx[0 + len(ss[0])] = True
dpy[0] = True
direct = 1
for s in ss[1:]:
    if direct % 2 == 0:
        tmp = dict()
        n = len(s)
        for (k, v) in list(dpx.items()):
            tmp[k + n] = True
            tmp[k - n] = True
        direct += 1
        dpx = tmp
    else:
        tmp = dict()
        n = len(s)
        for (k, v) in list(dpy.items()):
            tmp[k + n] = True
            tmp[k - n] = True
        direct += 1
        dpy = tmp
if x in dpx and y in dpy:
    print('Yes')
else:
    print('No')
