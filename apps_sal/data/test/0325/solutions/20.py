from collections import deque
def solve():
    N, M, P = map(int, input().split())
    G = [[] for i in range(N)]
    RG = [[] for i in range(N)]
    for i in range(M):
        a, b, c = map(int, input().split())
        G[a-1].append((b-1, P-c))
        RG[b-1].append((a-1, P-c))

    def chk(s, G):
        P = [0]*N
        que = deque([s])
        used = [0]*N
        used[s] = 1
        while que:
            v = que.popleft()
            P[v] = 1
            for w, c in G[v]:
                if used[w]:
                    continue
                que.append(w)
                used[w] = 1
        return P
    P0 = chk(0, G); P1 = chk(N-1, RG)
    F = [P0[i] == P1[i] == 1 for i in range(N)]
    I = [i for i in range(N) if F[i]]

    E0 = []
    for v in I:
        for w, c in G[v]:
            if not F[w]:
                continue
            E0.append((v, w, c))

    dist = [10**18]*N
    dist[0] = 0
    L = len(I)
    for i in range(L):
        update = 0
        for v, w, c in E0:
            x = c + dist[v]
            if x < dist[w]:
                dist[w] = x
                update = 1
        if not update:
            break
    else:
        print("-1")
        return

    print(max(-dist[N-1], 0))
solve()
