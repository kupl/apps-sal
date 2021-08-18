n, m, s, t = list(map(int, input().split()))
G = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = list(map(int, input().split()))
    G[a].append(b)
    G[b].append(a)

dists = [n + 1] * (n + 1)
distt = [n + 1] * (n + 1)

T = [s]
count = 0
while T:
    newT = []
    for i in T:
        dists[i] = min(dists[i], count)
        for j in G[i]:
            if dists[j] == n + 1:
                newT.append(j)
    count += 1
    T = newT

T = [t]
count = 0
while T:
    newT = []
    for i in T:
        distt[i] = min(distt[i], count)
        for j in G[i]:
            if distt[j] == n + 1:
                newT.append(j)
    count += 1
    T = newT

count = 0
mm = dists[t]
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if j in G[i]:
            continue
        if min(dists[i] + distt[j] + 1, dists[j] + distt[i] + 1) < mm:
            continue
        count += 1
print(count)
