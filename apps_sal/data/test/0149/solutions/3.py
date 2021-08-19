(a, b, c, d) = list(map(int, input().split(' ')))
MXV = 10 ** 18
(apows, bpows) = ([], [])
(aa, bb) = (1, 1)
while aa <= MXV:
    apows.append(aa)
    aa *= a
while bb <= MXV:
    bpows.append(bb)
    bb *= b
vals = set()
for i in range(len(apows)):
    for j in range(len(bpows)):
        vals.add(apows[i] + bpows[j])
vlist = list(vals)
vlist.sort()
ans = 0
last = c - 1
for v in vlist:
    if c <= v and v <= d:
        ans = max(ans, v - last - 1)
        last = v
ans = max(ans, d - last)
print(ans)
