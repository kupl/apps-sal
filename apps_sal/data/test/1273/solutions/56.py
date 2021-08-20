N = int(input())
G = [[] for n in range(N)]
vc = N * [0]
ec = (N - 1) * [0]
h = 1
for n in range(N - 1):
    (a, b) = map(int, input().split())
    G[a - 1].append((b - 1, n))
for (v, g) in enumerate(G):
    t = 1
    for (b, i) in g:
        if vc[v] == t:
            t += 1
        vc[b] = t
        ec[i] = t
        h = max(h, t)
        t += 1
print(h)
for n in range(N - 1):
    print(ec[n])
