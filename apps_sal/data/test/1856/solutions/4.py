import sys
input = sys.stdin.readline

m = 26
uf = [-1]*m
def root(x):
    if uf[x] < 0:
        return x
    uf[x] = root(uf[x])
    return uf[x]
def unite(x,y):
    rx, ry = root(x), root(y)
    if rx == ry:
        return False
    if uf[rx] > uf[ry]:
        rx, ry = ry, rx
    uf[rx] += uf[ry]
    uf[ry] = rx
    return True

n = int(input())
used = [0]*m
for i in range(n):
    s = input()[:-1]
    s = list(set(ord(c)-ord("a") for c in s))
    l = len(s)
    for j in range(l):
        used[s[j]] = 1
        for k in range(j+1, l):
            unite(s[j], s[k])
ans = sum(uf[i]<0 and used[i] for i in range(m))
print(ans)
