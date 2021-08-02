import math


class Glass:
    def __init__(self, pos, size, fill=0):
        self.s, self.p, self.f = size, pos, fill


n, w = map(int, input().split())
gls = []
sizes = [int(i) for i in input().split()]
for i in range(n):
    g = Glass(i, sizes[i])
    l = math.ceil(g.s / 2)
    if w >= l:
        g.f, w = l, w - l
        gls.append(g)
    else:
        print(-1)
        return
gls.sort(key=lambda y: y.s)
for i in range(n - 1, -1, -1):
    emp = gls[i].s - gls[i].f
    if w > 0:
        gls[i].f += min(emp, w)
        w -= min(emp, w)
    else:
        break

gls.sort(key=lambda y: y.p)
for i in range(n):
    print(gls[i].f, end=" ")
