n = int(input())
deg = [0 for _ in range(n + 1)]
chd = [0 for _ in range(n + 1)]
f = [0 for _ in range(n + 1)]
for i in range(2, n + 1):
    f[i] = int(input())
    deg[f[i]] += 1
isok = True
for i in range(2, n + 1):
    if deg[i] == 0:
        chd[f[i]] += 1
for i in range(1, n + 1):
    if deg[i] != 0 and chd[i] < 3:
        isok = False
if isok:
    print('Yes')
else:
    print('No')
