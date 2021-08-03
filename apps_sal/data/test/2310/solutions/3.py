import sys
n = int(input())
for i in range(n):
    sys.stdin.readline()
    q, w = map(int, sys.stdin.readline().split())
    kol = list(map(int, sys.stdin.readline().split()))
    r = []
    e = []
    for ii in range(q - 1):
        a, s = map(int, sys.stdin.readline().split())
        a -= 1
        r.append(a)
        e.append(s)
    rw = [0 for uu in kol]
    for ii in range(q - 1):
        if r[ii] != -1:
            rw[r[ii]] += 1
    nd = [0 for uu in kol]
    l = [uu for uu in kol]
    rez = [False for uu in kol]
    qw = 0
    tr = True
    for ii in range(q - 1):
        if e[ii] == 1 and tr:
            su = []
            for iii in range(w):
                if nd[iii] < rw[iii]:
                    continue
                if l[iii] > qw:
                    continue
                su.append(iii)
            if len(su) == 0:
                raise AssertionError
            for iii in su:
                rez[iii] = True
            qw -= min(map(lambda iii: l[iii], su))
            tr = False
        if r[ii] != -1:
            l[r[ii]] -= 1
            nd[r[ii]] += 1
            if l[r[ii]] == 0:
                tr = False
        else:
            qw += 1
    for iii in range(w):
        if l[iii] <= qw:
            rez[iii] = True
    sys.stdout.write(''.join(map(lambda x: 'Y' if x else 'N', rez)) + '\n')
