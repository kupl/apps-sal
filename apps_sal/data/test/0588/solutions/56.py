n = int(input())
pi = 3.141592653589793238462643383279
xy = [list(map(int, input().split())) for _ in range(n)]
import math

atan = [math.atan2(x[0], x[1]) for x in xy]
d = []


def hoge(a):
    ret = 0
    if a % (2*pi) < pi:
        ret = (a % pi)
    elif a % (2*pi)  > pi:
        ret = (a % pi)-pi
    else:
        ret = (a)
    #assert pi <= ret <= pi, 'range over'
    return ret  # -pi <= a <= pi


def seikika(A):
    ret = []
    for a in A:
        ret.append(hoge(a))
    return ret


gyoukaku = atan.copy()
gyoukaku.extend(seikika([a + pi for a in atan]))
M=60
for m in range(M):
    gyoukaku.extend(seikika([a + pi*(2*pi/M*m) for a in atan]))


def dist(xy):
    xx = sum([x[0] for x in xy])
    yy = sum([y[1] for y in xy])
    return (xx ** 2 + yy ** 2) ** 0.5


for g in gyoukaku:
    anglist = seikika([hoge(a - g) for a in atan])
    anglist = seikika(anglist)
    finalxy = []
    for i in range(n):
        if -pi / 2 -0.000001 <= anglist[i] <= pi / 2+0.000001:
            finalxy.append(xy[i])
    d.append(dist(finalxy))

print((max(d)))

