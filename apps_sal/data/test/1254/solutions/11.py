(n, m) = list(map(int, input().split()))
l = [list() for i in range(m)]
for i in range(n):
    (a, b) = list(map(int, input().split()))
    l[a - 1].append(b)
ss = []
for i in l:
    ii = sorted(i)
    ii.reverse()
    s = 0
    i.clear()
    for c in ii:
        s += c
        if s >= 0:
            i.append(c)
    i.sort()
    ss.append(sum(i))
ind = list(range(m))
s = 0
m = 0
while len(ind) > 0:
    nind = []
    sub = 0
    for i in ind:
        ll = l[i]
        if len(ll) > 0:
            s += ll.pop()
        if len(ll) > 0:
            nind.append(i)
        else:
            sub += ss[i]
    m = max(m, s)
    s -= sub
    ind = nind
print(m)
