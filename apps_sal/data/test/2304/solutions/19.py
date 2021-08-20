def main():
    from collections import deque
    import sys
    input = sys.stdin.readline
    (N, M) = list(map(int, input().split()))
    g = tuple((set() for _ in range(N)))
    h = [0] * N
    for _ in range(M):
        (L, R, D) = list(map(int, input().split()))
        L -= 1
        R -= 1
        g[L].add((R, D))
        h[R] += 1
    dist = [-1] * N

    def dfs(s):
        dist[s] = 0
        dq = deque([s])
        while dq:
            v = dq.popleft()
            for (u, d) in g[v]:
                if ~dist[u]:
                    if dist[u] != dist[v] + d:
                        return False
                else:
                    dist[u] = dist[v] + d
                    dq.append(u)
        return True
    for s in range(N):
        if h[s]:
            continue
        if not dfs(s):
            print('No')
            return
    for s in range(N):
        if ~dist[s]:
            continue
        if not dfs(s):
            print('No')
            return
    print('Yes')


def __starting_point():
    main()


__starting_point()
