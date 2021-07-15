import bisect
ind = {}
s = input()
t = input()
for i, c in enumerate(s):
    if c in ind:
        ind[c].append(i+1)
    else:
        ind[c] = [i+1]
k = len(s)
nk = 0
if not t[0] in ind:
    print(-1)
    return
nw = ind[t[0]][0]
pv = nw
for i in range(1, len(t)):
    c = t[i]
    if not c in ind:
        print(-1)
        return
    if ind[c][-1]>pv:
        pv = ind[c][bisect.bisect_left(ind[c], pv+1)]
    else:
        nk += k
        pv = ind[c][0]
    nw = pv + nk
print(nw)
