(n, m) = map(int, input().split())
d = [[] for i in range(3)]
res_odd = 0
res_even = 0
for i in range(n):
    (t1, t2) = map(int, input().split())
    d[t1 - 1].append(t2)
d[0].sort()
d[2].sort(reverse=True)
c = d[1].copy()
if d[0]:
    i = len(d[0]) - 2
    while i >= 1:
        c.append(d[0][i] + d[0][i - 1])
        i -= 2
    c.sort(reverse=True)
    pref = [0 for i in range(len(c) + 1)]
    pref[0] = 0
    for i in range(1, len(c) + 1):
        pref[i] = pref[i - 1] + c[i - 1]
    p = 0
    for i in range(min(len(d[2]), (m - 1) // 3) + 1):
        if i != 0:
            p += d[2][i - 1]
        res_odd = max(res_odd, d[0][-1] + p + pref[min(max(m - i * 3 - 1, 0) // 2, len(pref) - 1)])
i = len(d[0]) - 1
while i >= 1:
    d[1].append(d[0][i] + d[0][i - 1])
    i -= 2
d[1].sort(reverse=True)
pref = [0 for i in range(len(d[1]) + 1)]
pref[0] = 0
for i in range(1, len(d[1]) + 1):
    pref[i] = pref[i - 1] + d[1][i - 1]
p = 0
for i in range(min(len(d[2]), m // 3) + 1):
    if i != 0:
        p += d[2][i - 1]
    res_even = max(res_even, p + pref[min(max(m - i * 3, 0) // 2, len(pref) - 1)])
print(max(res_odd, res_even))
