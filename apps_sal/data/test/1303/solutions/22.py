x1 = []
x2 = []
(p, q, l, r) = map(int, input().split(' '))
for i in range(p):
    (a, b) = map(int, input().split(' '))
    x1.append([a, b])
for i in range(q):
    (a, b) = map(int, input().split(' '))
    x2.append([a, b])
ok2 = []
for a in x1:
    for b in x2:
        lo = a[0] - b[1]
        hi = a[1] - b[0]
        if hi >= r:
            hi = r
        if lo <= l:
            lo = l
        ok2.append([lo, hi])
ok = [i for i in ok2 if i[1] >= i[0]]
ok.sort()
total = 0
if len(ok) == 0:
    print(0)
else:
    intv = ok[0]
    for i in range(1, len(ok)):
        curr = ok[i]
        if curr[0] > intv[1]:
            if intv[1] == intv[0]:
                total += 1
            else:
                total += intv[1] - intv[0] + 1
            intv = curr
        else:
            minim = [min(curr[0], intv[0]), max(curr[1], intv[1])]
            intv = minim
    if intv[1] == intv[0]:
        total += 1
    else:
        total += intv[1] - intv[0] + 1
    print(total)
