import sys


def main():

    n, w, v, u = list(map(int, sys.stdin.readline().split()))

    c = []
    for i in range(n):
        c.append(list(map(int, sys.stdin.readline().split())))

    ymin = 10**9 + 1
    iymin = 0
    ymax = -1
    iymax = 0
    xmax = -1
    ixmax = 0
    for i in range(n):
        if c[i][1] < ymin:
            ymin = c[i][1]
            iymin = i
        if c[i][1] > ymax:
            ymax = c[i][1]
            iymax = i
        if c[i][0] > xmax:
            xmax = c[i][0]
            ixmax = i

    jmin = (iymin - 1 + n) % n
    while ymin == c[jmin][1]:
        jmin = (jmin - 1 + n) % n
    iymin = (jmin + 1) % n

    jmax = (iymax + 1) % n
    while ymax == c[jmax][1]:
        jmax = (jmax + 1) % n
    iymax = (jmax - 1 + n) % n

    jcur = iymin
    ok = True
    finish = (iymax - 1 + n) % n
    while jcur != finish:
        ta = c[jcur][0] / v
        if ta < c[jcur][1] / u:
            ok = False
            break
        jcur = (jcur - 1 + n) % n

    if ok:
        print("%.8f" % (w / u))
        return

    jmin = (iymin + 1) % n
    while ymin == c[jmin][1]:
        jmin = (jmin + 1) % n
    iymin = (jmin - 1 + n) % n

    jmax = (ixmax + 1) % n
    while xmax == c[jmax][0]:
        jmax = (jmax + 1) % n
    ixmax = (jmax - 1 + n) % n

    t = 0
    jcur = iymin
    cury = 0
    finish = (ixmax + 1) % n
    while jcur != finish:
        l = c[jcur][1] - cury

        ta = c[jcur][0] / v
        tp = l / u
        t = max(t + tp, ta)

        cury += l
        jcur = (jcur + 1) % n

    t += (w - cury) / u

    print("%.8f" % t)


main()
