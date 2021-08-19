(n, s, *a) = map(int, open(0).read().split())
d = [0] * 3001
c = 0
for (i, a) in enumerate(a):
    for j in range(s - a, 0, -1):
        d[a + j] += d[j]
    d[a] -= ~i
    c += d[s]
print(c % 998244353)
