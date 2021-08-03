from collections import Counter
b = [int(i) for i in list(input())]
a = [int(i) for i in list(input())]
if len(b) < len(a):
    print(''.join([str(i) for i in sorted(b, key=lambda x: -x)]))
    return
bs = Counter(b)
mp = 0
while mp < len(a) and bs[a[mp]] > 0:
    bs[a[mp]] -= 1
    mp += 1
if mp == len(a):
    print(''.join(str(i) for i in a))
    return

ms = 0
for s in range(1, mp + 1):
    bs = Counter(b)
    for i in range(s):
        bs[a[i]] -= 1
    nl = a[s] - 1
    while nl >= 0 and bs[nl] == 0:
        nl -= 1
    if nl == -1:
        continue
    else:
        ms = s
ans = []
bs = Counter(b)
for i in range(ms):
    bs[a[i]] -= 1
    ans.append(a[i])
nl = a[ms] - 1
while nl >= 0 and bs[nl] == 0:
    nl -= 1
ans.append(nl)
bs[nl] -= 1
d1 = [[i for _ in range(bs[i])] for i in bs]
r = []
for l in d1:
    r += l
r = sorted(r, key=lambda x: -x)
ans += r
print(''.join([str(i) for i in ans]))
