from heapq import heappush, heappop
def main():
    N, M, S = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v, a, b = list(map(int, input().split()))
        u -= 1
        v -= 1
        G[u].append((v, a, b))
        G[v].append((u, a, b))
    CD = [list(map(int, input().split())) for _ in range(N)]
    distance = [[1<<62]*2501 for _ in range(N)]
    q = [(0, 0, min(S, 2500))]
    distance[0][min(S, 2500)] = 0
    while q:
        d, v, vs = heappop(q)
        if distance[v][vs] != d:
            continue

        vc, vd = CD[v]
        ud = d + vd
        us = vs + vc
        if us > 2500:
            us = 2500
        if distance[v][us] > ud:
            distance[v][us] = ud
            heappush(q, (ud, v, us))

        for u, fee, b in G[v]:
            if fee > vs:
                continue
            ud = d + b
            us = vs - fee
            if us > 2500:
                us = 2500
            if distance[u][us] > ud:
                distance[u][us] = ud
                heappush(q, (ud, u, us))
    print(("\n".join(str(min(d)) for d in distance[1:])))

main()

