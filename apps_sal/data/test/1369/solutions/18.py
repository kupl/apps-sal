from math import sqrt
import itertools
N = int(input())
P = []
for i in range(N):
    P.append(list(map(int, input().split())))


def dist(P, Q):
    return sqrt((P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2)


def isFound(R):
    for (i, j) in itertools.combinations(list(range(N)), 2):
        if dist(P[i], P[j]) >= 2 * R:
            continue
        (x1, y1) = P[i]
        (x2, y2) = P[j]
        PM = dist(P[i], P[j]) / 2
        (xm, ym) = ((x1 + x2) / 2, (y1 + y2) / 2)
        (x_ev, y_ev) = (y2 - y1, x1 - x2)
        norm_ev = sqrt(x_ev ** 2 + y_ev ** 2)
        (x_ev, y_ev) = (x_ev / norm_ev, y_ev / norm_ev)
        MM = sqrt(R ** 2 - PM ** 2)
        P1 = [xm + x_ev * MM, ym + y_ev * MM]
        P2 = [xm - x_ev * MM, ym - y_ev * MM]
        for v in [P1, P2]:
            flg = False
            for p in P:
                if dist(v, p) > R + 1e-07:
                    flg = True
                    break
            if flg:
                continue
            else:
                return True
    return False


(l, r) = (0, 1001)
for i in range(100):
    m = (l + r) / 2
    if isFound(m):
        r = m
    else:
        l = m
print(m)
