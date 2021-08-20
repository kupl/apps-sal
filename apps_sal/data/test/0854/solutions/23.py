(n, t) = list(map(int, input().split()))
a = [list(map(int, input().split()))]
k = 0
na = 0
ma = 1
while t >= ma:
    sa = sum(a[na])
    la = len(a[na])
    if t >= sa:
        k += la * (t // sa)
        t %= sa
    ma = min(a[na])
    a.append([])
    for ta in a[na]:
        if t >= ta:
            t -= ta
            k += 1
            a[na + 1].append(ta)
    na += 1
print(k)
