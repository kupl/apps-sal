(n, m) = list(map(int, input().split()))
d = {i + 1: [] for i in range(n)}
for i in range(m):
    (a, b) = list(map(int, input().split()))
    d[a].append(b)
    d[b].append(a)
maxln = len(d[1])
maxel = 1
for i in d:
    if len(d[i]) > maxln:
        maxel = i
        maxln = len(d[i])
l = [maxel]
k = 0
visit = [0 for i in range(n)]
visit[maxel - 1] = 1
while k < len(l):
    for i in range(len(d[l[k]])):
        if visit[d[l[k]][i] - 1] == 0:
            print(d[l[k]][i], l[k])
            visit[d[l[k]][i] - 1] = 1
            l.append(d[l[k]][i])
    k += 1
