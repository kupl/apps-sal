n = int(input())
n1 = n - 2
d = {}
d1 = {}
visit = {}
l1 = []
for i in range(1, n + 1):
    d[i] = []
    d1[i] = 0
    visit[i] = False
while n1:
    n1 -= 1
    (a, b, c) = list(map(int, input().split()))
    d[a].append(b)
    d[a].append(c)
    d1[a] += 1
    d[b].append(a)
    d[b].append(c)
    d1[b] += 1
    d[c].append(b)
    d[c].append(a)
    d1[c] += 1
d1 = dict(sorted(list(d1.items()), key=lambda x: x[1]))
for i in d1:
    if not visit[i]:
        visit[i] = True
        l1.append(i)
    x = sorted(d[i], key=lambda x: d1[x])
    for j in x:
        if not visit[j]:
            visit[j] = True
            l1.append(j)
            x += d[j]
print(*l1)
