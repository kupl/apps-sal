def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    N, M = list(map(int, input().split()))

    g = tuple(set() for _ in range(N))
    h = [0] * N  # 入り次数
    for _ in range(M):
        L, R, D = list(map(int, input().split()))
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
            for u, d in g[v]:
                if ~dist[u]:
                    if dist[u] != dist[v] + d:
                        return False
                else:
                    dist[u] = dist[v] + d
                    dq.append(u)
        return True

    # 始点からのパスを処理
    for s in range(N):
        if h[s]: continue  # sに入ってくるパスがあるので、sを始点にしない
        if ~dist[s]: continue
        if not dfs(s):
            print('No')
            return

    # サイクルを処理（どの点も入るパスがあり、処理できていない）
    for s in range(N):
        if ~dist[s]: continue
        if not dfs(s):
            print('No')
            return

    print('Yes')


def __starting_point():
    main()

__starting_point()
