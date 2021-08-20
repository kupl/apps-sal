(n, s) = map(int, input().split())
buy = dict()
sell = dict()
for i in range(n):
    (d, p, q) = map(str, input().split())
    p = int(p)
    q = int(q)
    if d == 'B':
        if p in buy:
            buy[p] += q
        else:
            buy[p] = q
    elif p in sell:
        sell[p] += q
    else:
        sell[p] = q
bk = list(buy.keys())
bv = list(buy.values())
bl = list(zip(bk, bv))
sk = list(sell.keys())
sv = list(sell.values())
sl = list(zip(sk, sv))
bl.sort(reverse=True)
sl.sort()
bb = len(bl)
ss = len(sl)
if s > ss:
    sl.sort(reverse=True)
    for i in range(ss):
        print('S', sl[i][0], sl[i][1])
else:
    sl.sort()
    for i in range(s - 1, -1, -1):
        print('S', sl[i][0], sl[i][1])
if s > bb:
    for i in range(bb):
        print('B', bl[i][0], bl[i][1])
else:
    for i in range(s):
        print('B', bl[i][0], bl[i][1])
