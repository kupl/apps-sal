from collections import defaultdict as dd
MOD = 10**9 + 7
I = lambda: list(map(int, input().split()))
n, = I()
d = dd(list)
for i in range(n - 1):
    t = I()
    d[t[0]].append(t[1])
    d[t[1]].append(t[0])
l = I()
v = [0] * (n + 1)
s = 1
what = 0
v[1] = 1
while what < s:
    a = set()
    i = l[what]
    for j in d[i]:
        if not v[j]:
            a.add(j)
    b = set()
    for j in range(s, s + len(a)):
        b.add(l[j])
    if a != b:
        print('No')
        return
    kkk = 0
    for k in a:
        kkk += 1
        v[k] = 1
    s += kkk
    what += 1
if s != n:
    print('No')
    return
print('Yes')
