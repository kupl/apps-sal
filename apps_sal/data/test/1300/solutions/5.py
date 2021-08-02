t = list(map(int, input().split()))
n = t[0]
c = t[1]
a = list(map(int, input().split()))
f = []
for i in range(0, 500001):
    f.append(0)
l = []
for i in range(0, 500001):
    l.append([0])
m = 0
for i in range(n):
    l[a[i]].append(f[a[i]] - m)
    if a[i] == c:
        m += 1
    f[a[i]] += 1
    l[a[i]].append(f[a[i]] - m)
ma = 0
for i in l:
    mi = 0
    for j in i:
        if(j < mi):
            mi = j
        if(ma < j - mi):
            ma = j - mi
print(m + ma)
