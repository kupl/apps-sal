import bisect
import math
import sys
input = sys.stdin.readline
(n, m, cl, ce, v) = list(map(int, input().split()))
l = [int(i) for i in input().split() if i != '\n']
e = [int(i) for i in input().split() if i != '\n']
q = int(input())
for i in range(q):
    (x1, y1, x2, y2) = list(map(int, input().split()))
    (lft, neareststa, sta, nearestele) = (0, 0, 0, 0)
    if x2 == x1 and y1 == y2:
        output = 0
    elif x2 == x1:
        output = abs(y2 - y1)
    else:
        lft = math.ceil(abs(x2 - x1) / v)
        sta = abs(x2 - x1)
        if cl > 0:
            nearestele = bisect.bisect_left(l, y1)
            if len(l) > nearestele:
                first = abs(l[nearestele] - y1) + abs(y2 - l[nearestele])
            else:
                first = 1000000000001
            if nearestele != 0:
                second = abs(l[nearestele - 1] - y1) + abs(y2 - l[nearestele - 1])
            else:
                second = 1000000000001
            nearestele = min(first, second)
        else:
            nearestele = 1000000000001
        if ce > 0:
            neareststa = bisect.bisect_left(e, y1)
            if len(e) > neareststa:
                first = abs(e[neareststa] - y1) + abs(y2 - e[neareststa])
            else:
                first = 1000000000001
            if neareststa != 0:
                second = abs(e[neareststa - 1] - y1) + abs(y2 - e[neareststa - 1])
            else:
                second = 1000000000001
            neareststa = min(first, second)
        else:
            neareststa = 1000000000001
        output = min(lft + neareststa, sta + nearestele)
    sys.stdout.write(str(output) + '\n')
