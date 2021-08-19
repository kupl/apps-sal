import sys
ls = []
ss = []
rs = []
ps = []
for __ in range(4):
    (l, s, r, p) = [int(elem) == 1 for elem in sys.stdin.readline().split()]
    ls.append(l)
    ss.append(s)
    rs.append(r)
    ps.append(p)


def get(ary, indx):
    return ary[indx % 4]


accident = False
for indx in range(4):
    accident |= (ls[indx] or rs[indx] or ss[indx]) and ps[indx]
    accident |= ls[indx] and get(ps, indx - 1)
    accident |= ss[indx] and get(ps, indx + 2)
    accident |= rs[indx] and get(ps, indx + 1)
if accident:
    print('YES')
else:
    print('NO')
