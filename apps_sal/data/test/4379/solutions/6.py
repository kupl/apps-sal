n = int(input())
a = list(map(int, input().split()))
d = dict()
opt = []
m = -1
for i in range(n):
    t = a[i]
    p = t - 1
    if p in d:
        if (t not in d) or ((p - d[p]) >= (t - d[t])):
            d[t] = d[p]
            k = t - d[t]
            if k > m:
                m = k
                opt = d[t]
    else:
        if t not in d:
            d[t] = t
            if m == -1:
                opt = t
                m = 0
print(m + 1)
r = []
for i in range(n):
    if a[i] == opt:
        r += [i + 1]
        opt += 1
print(*r)
