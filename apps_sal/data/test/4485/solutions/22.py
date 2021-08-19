(N, M) = list(map(int, input().split()))
G = [list() for _ in range(N)]
for _ in range(M):
    (a, b) = list(map(int, input().split()))
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
G[0].sort()
G[N - 1].sort()
i = 0
j = 0
while i < len(G[0]) and j < len(G[N - 1]):
    if G[0][i] == G[N - 1][j]:
        print('POSSIBLE')
        break
    elif G[0][i] < G[N - 1][j]:
        i += 1
    else:
        j += 1
else:
    print('IMPOSSIBLE')
