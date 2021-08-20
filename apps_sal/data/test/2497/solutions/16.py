from collections import defaultdict
N = int(input())
(xlist, ylist) = ([], [])
for i in range(N):
    (xs, ys, d) = input().split()
    x = int(xs)
    y = int(ys)
    if d == 'L':
        xlist.append((x, -1))
        ylist.append((y, 0))
    elif d == 'R':
        xlist.append((x, 1))
        ylist.append((y, 0))
    elif d == 'U':
        xlist.append((x, 0))
        ylist.append((y, 1))
    else:
        xlist.append((x, 0))
        ylist.append((y, -1))
xdic = defaultdict(set)
for (x, d) in xlist:
    xdic[d].add(x)
xlist2 = []
for d in [-1, 0, 1]:
    if len(xdic[d]):
        min_d = min(xdic[d])
        max_d = max(xdic[d])
        xlist2.append((min_d, d))
        xlist2.append((max_d, d))
ydic = defaultdict(set)
for (y, d) in ylist:
    ydic[d].add(y)
ylist2 = []
for d in [-1, 0, 1]:
    if len(ydic[d]):
        min_d = min(ydic[d])
        max_d = max(ydic[d])
        ylist2.append((min_d, d))
        ylist2.append((max_d, d))


def cand_time(plist):
    ret = set()
    for i in range(len(plist)):
        (p1, d1) = plist[i]
        for j in range(i + 1, len(plist)):
            (p2, d2) = plist[j]
            if d1 == d2:
                continue
            if d1 == -1:
                if d2 == 0:
                    t = p1 - p2
                else:
                    t = (p1 - p2) / 2
            elif d1 == 0:
                if d2 == -1:
                    t = p2 - p1
                else:
                    t = p1 - p2
            elif d2 == -1:
                t = (p2 - p1) / 2
            else:
                t = p2 - p1
            if t > 0:
                ret.add(t)
    return ret


cand_time_x = cand_time(xlist2)
cand_time_y = cand_time(ylist2)
cand_t = [0] + list(cand_time_x) + list(cand_time_y)


def get_pos(pd, t):
    (p, d) = pd
    return p + d * t


answer = float('inf')
for t in cand_t:
    pos_min_x = float('inf')
    pos_max_x = -float('inf')
    for x2 in xlist2:
        pos_min_x = min(pos_min_x, get_pos(x2, t))
        pos_max_x = max(pos_max_x, get_pos(x2, t))
    pos_min_y = float('inf')
    pos_max_y = -float('inf')
    for y2 in ylist2:
        pos_min_y = min(pos_min_y, get_pos(y2, t))
        pos_max_y = max(pos_max_y, get_pos(y2, t))
    t_ans = abs(pos_max_x - pos_min_x) * abs(pos_max_y - pos_min_y)
    if answer >= t_ans:
        answer = t_ans
print(answer)
