import sys
input = sys.stdin.readline
n = int(input())
f = []
d = []
for i in range(0, 26):
    d.append([0] * 26)
use = [0] * 26
for i in range(0, 26):
    f.append(i)


def find(x):
    if x != f[x]:
        f[x] = find(f[x])
    return f[x]


for i in range(0, n):
    l = []
    for j in set(input().rstrip()):
        use[ord(j) - 97] = 1
        l.append(ord(j) - 97)
    ll = len(l)
    for k in range(0, ll):
        for j in range(k + 1, ll):
            d[l[k]][l[j]] = 1
for i in range(0, 26):
    for j in range(0, 26):
        if d[i][j]:
            if find(i) != find(j):
                f[find(i)] = find(j)
ans = []
a = 0
for i in range(0, 26):
    if use[i] == 1 and find(i) not in ans:
        ans.append(find(i))
        a += 1
print(a)
