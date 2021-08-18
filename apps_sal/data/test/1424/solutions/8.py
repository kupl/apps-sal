v = list(int(x) for x in input().split())
n = v[0]
m = v[1]
k = v[2]
v = list()
for i in range(m + 1):
    v.append(int(input()))
f = bin(v[m])[2:]
f = ('0' * (n - len(f))) + f
tot = 0
for i in range(m):
    c = 0
    t = bin(v[i])[2:]
    t = ('0' * (n - len(t))) + t
    for j in range(n):
        if t[j] != f[j]:
            c += 1
    if c <= k:
        tot += 1
print(tot)
