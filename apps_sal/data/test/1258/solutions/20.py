rinp = [4, 6, 2, 1, 7, 3, 5]
'\n7\n4 6 2\n6 2 1\n2 1 7\n1 7 3\n7 3 5\n'
n = int(input())
ans = list()
BIN = list(((i, list()) for i in range(n)))
i = 2
while i < n:
    inp = list((int(x) - 1 for x in input().split()))
    for ch in inp:
        BIN[ch][1].append(inp)
    i += 1
SB = sorted(BIN, key=lambda x: len(x[1]))
now = SB[0][0]
last = None
while True:
    ans.append(now)
    nowl = BIN[now][1]
    lnowl = len(nowl)
    if lnowl == 3:
        for item in nowl:
            try:
                item.remove(now)
            except:
                pass
            try:
                item.remove(last)
            except:
                pass
            if len(item) == 1:
                next = item[0]
                break
    elif lnowl == 2:
        for item in nowl:
            try:
                item.remove(now)
            except:
                pass
            try:
                item.remove(last)
            except:
                pass
            if len(item) == 1:
                next = item[0]
                break
    else:
        tl = nowl[0]
        tl.remove(now)
        if not tl:
            break
        for next in tl:
            ttl = BIN[next][1]
            if len(ttl) == 2:
                break
    (now, last) = (next, now)
print(' '.join((str(x + 1) for x in ans)))
