N = int(input())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
G = [[] for i in range(N)]
INF = float('inf')
for i in range(1, N):
    G[f[i - 1] - 1].append(i)

d = [0] * N
k = 0
for i in range(N - 1, -1, -1):
    if len(G[i]) == 0:
        d[i] = 1
        k += 1
        continue

    if a[i] == 0:
        d[i] = 0
        for j in G[i]:
            d[i] += d[j]
    else:
        d[i] = INF
        for j in G[i]:
            d[i] = min(d[i], d[j])

print(k - d[0] + 1)

