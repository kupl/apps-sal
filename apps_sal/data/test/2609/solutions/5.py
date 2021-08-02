from sys import stdin
input = stdin.readline
q = int(input())
for rwere in range(q):
    n = int(input())
    seg = []
    pts = []
    for i in range(n):
        pocz, kon = map(int, input().split())
        seg.append([2 * pocz, 2 * kon])
        pts.append(2 * kon + 1)
    p, k = map(list, zip(*seg))
    pts += (p + k)
    pts.sort()
    ind = -1
    while True:
        if pts[ind] == pts[-1]:
            ind -= 1
        else:
            break
    ind += 1
    pts = pts[:ind]
    mapa = {}
    val = 0
    mapa[pts[0]] = val
    for i in range(1, len(pts)):
        if pts[i] != pts[i - 1]:
            val += 1
        mapa[pts[i]] = val
    val += 1
    for i in range(n):
        seg[i] = [mapa[seg[i][0]], mapa[seg[i][1]]]
    seg.sort()
    dupa = [0] * (val + 1)
    for s in seg:
        dupa[s[0]] += 1
        dupa[s[1] + 1] -= 1
    cov = [0] * val
    cov[0] = dupa[0]
    for i in range(1, val):
        cov[i] = cov[i - 1] + dupa[i]
    przyn = [0] * val
    cur = seg[0][0]
    label = 1
    for i in range(n):
        kon = seg[i][1]
        if cur <= kon:
            for j in range(cur, kon + 1):
                przyn[j] = label
            label += 1
            cur = kon + 1
    final = [(przyn[i] if cov[i] == 1 else (-1 if cov[i] == 0 else 0)) for i in range(val)]
    baza = final.count(-1) + 1
    final = [-1] + final + [-1]
    val += 2
    if max(final) <= 0:
        print(baza)
    else:
        comp = {}
        comp[0] = -100000000000
        for i in final:
            if i > 0:
                comp[i] = 0
        for i in range(1, val - 1):
            if final[i] > 0 and final[i] != final[i - 1]:
                comp[final[i]] += 1
            if final[i - 1] == -1:
                comp[final[i]] -= 1
            if final[i + 1] == -1:
                comp[final[i]] -= 1
        best = -10000000000000
        for i in comp:
            best = max(best, comp[i])
        if max(final) == n:
            print(baza + best)
        else:
            print(max(baza + best, baza))
