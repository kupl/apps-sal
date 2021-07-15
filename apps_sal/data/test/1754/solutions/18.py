kol = 0
n, m, k = map(int,input().split())
p = list(map(int,input().split()))
s = list(map(int,input().split()))
for i in range(n):
    s[i] -= 1
c = list(map(int,input().split()))
for i in range(k):
    c[i] -= 1
sc = [[] for i in range(m)]
for i in range(n):
    sc[s[i]].append([p[i], i])
for i in range(m):
    sc[i] = sorted(sc[i])
for i in range(k):
    if sc[s[c[i]]][-1][0] != p[c[i]]:
        kol += 1
print(kol)
