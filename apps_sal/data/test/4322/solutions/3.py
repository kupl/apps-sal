def kk(): return map(int, input().split())
def ll(): return list(kk())


n = int(input())
d = {}
for v in kk():
    if v not in d:
        d[v] = 0
    d[v] += 1
k = list(d.keys())
k.sort()
i = 0
m = 0
while i < len(k):
    start = x = k[i]
    total = d[start]
    while i + 1 < len(k) and k[i] + 1 == k[i + 1]:
        i += 1
        total += d[k[i]]
        if d[k[i]] == 1:
            if total > m:
                m, mi = total, (start, k[i])
            break
    else:
        i += 1
        if total > m:
            m, mi = total, (start, k[i - 1])
print(m)
tbp = []
for i in range(mi[0], mi[1] + 1):
    tbp.extend([i] * (d[i] - 1))
print()
for i in range(mi[1], mi[0] - 1, -1):
    tbp.append(i)
print(*tbp)
