(tn, tk) = input().split()
n = int(tn)
k = int(tk)
a = input()
vis = []
t = []
for i in range(n):
    t.append((a[i], i))
t.sort()
for i in range(n):
    vis.append(0)
for i in range(k):
    vis[t[i][1]] = 1
for i in range(n):
    if vis[i]:
        continue
    print(a[i], end='')
