n, m = list(map(int, input().split()))
a, s = [], []
for q in range(n):
    d = list(map(int, input().split()))
    a.append(d[0])
    s.append(d[1])
d = {}
for q in range(n):
    if a[q] in d:
        d[a[q]].append(s[q])
    else:
        d[a[q]] = [s[q]]
for q in d:
    d[q].sort(reverse=True)
for q in list(d.values()):
    sum1 = 0
    for q1 in range(len(q)):
        sum1 += q[q1]
        q[q1] = sum1
f = [0] * (len(max(list(d.values()), key=lambda x: len(x))) + 1)
for q in list(d.values()):
    for q1 in range(len(q)):
        if q[q1] > 0:
            f[q1] += q[q1]
print(max(f))
