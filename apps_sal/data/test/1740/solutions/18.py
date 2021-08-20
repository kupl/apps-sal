N = int(input())
P = [i for i in range(N)]
G = [[i] for i in range(N)]
for i in range(N - 1):
    (x, y) = map(int, input().split())
    (x, y) = (x - 1, y - 1)
    x = P[x]
    y = P[y]
    if len(G[x]) < len(G[y]):
        (x, y) = (y, x)
    G[x] += G[y]
    for k in G[y]:
        P[k] = x
print(' '.join(map(lambda x: str(x + 1), G[P[0]])))
