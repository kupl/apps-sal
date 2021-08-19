import bisect
INF = 10 ** 100
(A, B, Q, *stx) = open(0).read().split()
(A, B, Q) = map(int, [A, B, Q])
slist = [-INF] + [int(stx[i]) for i in range(A)] + [INF]
tlist = [-INF] + [int(stx[i]) for i in range(A, A + B)] + [INF]
xlist = [int(stx[i]) for i in range(A + B, A + B + Q)]
oslist = [0] * 2
otlist = [0] * 2
sr_index = 0
tr_index = 0
for i in xlist:
    ans = INF
    sr_index = bisect.bisect_left(slist, i)
    oslist = [slist[sr_index - 1], slist[sr_index]]
    tr_index = bisect.bisect_left(tlist, i)
    otlist = [tlist[tr_index - 1], tlist[tr_index]]
    for j in oslist:
        for k in otlist:
            ans = min(ans, abs(j - i) + abs(k - j), abs(k - i) + abs(j - k))
    print(ans)
