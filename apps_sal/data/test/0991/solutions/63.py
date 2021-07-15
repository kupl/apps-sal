#!python3

from heapq import heappop, heappush


INF = 10 ** 18

# input
N, M, S = list(map(int, input().split()))
UVAB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(N)]


def solve(link):
    ans = {}
    lim = 50 * (N - 1)
    w = [[INF] * (lim + 1) for _ in range(N)]

    # (time, node, silver)
    hq = [(0, 0, min(S, lim))]
    while hq:
        t, v, s = heappop(hq)
        if t > w[v][s]:
            continue
        if v not in ans:
            ans[v] = t
            if len(ans) == N:
                break
        
        # buy
        if s < lim:
            c, d = CD[v]
            new_s = min(lim, s + c)
            new_t = t + d
            if new_t < w[v][new_s]:
                w[v][new_s] = new_t
                heappush(hq, (new_t, v, new_s))
        
        # move
        for u, a, b in link[v]:
            if s < a:
                continue
            new_s = s - a
            new_t = t + b
            if new_t < w[u][new_s]:
                w[u][new_s] = new_t
                heappush(hq, (new_t, u, new_s))
        
    return ans


def main():
    link = [[] for _ in range(N)]
    for u, v, a, b in UVAB:
        link[u - 1].append((v - 1, a, b))
        link[v - 1].append((u - 1, a, b))
    
    ans = solve(link)
    for i in range(1, N):
        print((ans[i]))


def __starting_point():
    main()

__starting_point()
