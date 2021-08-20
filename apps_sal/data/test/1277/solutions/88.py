(N, u, v) = (int(i) for i in input().split())
adj = []
for i in range(N + 1):
    adj.append([])
for i in range(N - 1):
    (a, b) = list(map(int, input().split()))
    adj[a] += [b]
    adj[b] += [a]


def distances(sommet):
    d = [-1] * (N + 1)
    File = [sommet]
    d[sommet] = 0
    while File:
        s = File.pop()
        for x in adj[s]:
            if d[x] == -1:
                d[x] = 1 + d[s]
                File.append(x)
    return d


t = distances(u)
a = distances(v)
ans = -1
for i in range(1, N + 1):
    if t[i] < a[i]:
        ans = max(ans, a[i] - 1)
print(ans)
