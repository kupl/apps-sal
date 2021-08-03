def R(): return map(int, input().split())


n, temp = R()
a = list(R())
t = list(R())
v = sorted([(t[i] - temp, a[i]) for i in range(n)])

r = sum([v[i][1] for i in range(n) if v[i][0] == 0])
pos = sum([v[i][0] * v[i][1] for i in range(n) if v[i][0] > 0])
neg = sum([abs(v[i][0]) * v[i][1] for i in range(n) if v[i][0] < 0])

pa = sum([v[i][1] for i in range(n) if v[i][0] > 0])
na = sum([v[i][1] for i in range(n) if v[i][0] < 0])

if pos == 0 or neg == 0:
    print(r)
    return

for i in range(n):
    if v[i][0] >= 0:
        stn = i - 1
        break

for i in range(n):
    if v[i][0] > 0:
        stp = i
        break

if neg < pos:
    r += na
    rem = neg * 1.0
    for i in range(stp, n):
        if v[i][0] * v[i][1] >= rem:
            r += rem / v[i][0]
            rem = 0
        else:
            r += v[i][1]
            rem -= v[i][0] * v[i][1]
else:
    r += pa
    rem = pos * 1.0
    for i in reversed(range(stn + 1)):
        if abs(v[i][0]) * v[i][1] >= rem:
            r += rem / abs(v[i][0])
            rem = 0
        else:
            r += v[i][1]
            rem -= abs(v[i][0]) * v[i][1]

print(r)
