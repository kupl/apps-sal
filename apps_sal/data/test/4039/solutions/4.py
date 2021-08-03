
n, r = map(int, input().split())
aa = [0] * n
bb = [0] * n
for i in range(n):
    aa[i], bb[i] = map(int, input().split())
avail = set(range(n))
fr = r + sum(bb)
if fr < 0:
    print("NO")
    return
ok = True
for i in range(n):
    nxt = -1
    for j in avail:
        if aa[j] <= r and bb[j] >= 0:
            nxt = j
            break
    if nxt == -1:
        break
    avail.remove(nxt)
    r += bb[nxt]
for i in range(len(avail)):
    nxt = -1
    for j in avail:
        if aa[j] + bb[j] <= fr and bb[j] < 0:
            nxt = j
            break
    if nxt == -1:
        ok = False
        break
    avail.remove(nxt)
    fr -= bb[nxt]
if ok:
    print("YES")
else:
    print("NO")
