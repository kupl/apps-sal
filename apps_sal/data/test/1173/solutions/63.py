import sys
input = sys.stdin.readline


def main():
    N = int(input())
    Id = {}
    cur = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            Id[i, j] = cur
            cur += 1
    G = [[] for i in range(N * (N - 1) // 2)]
    size = [0] * (N * (N - 1) // 2)
    for i in range(1, N + 1):
        for (idx, j) in enumerate(list(map(int, input().split()))):
            if i < j:
                k = Id[i, j]
            else:
                k = Id[j, i]
            if idx:
                G[par].append(k)
                size[k] += 1
            par = k
    g = [idx for (idx, s) in enumerate(size) if s == 0]
    ans = 0
    while g:
        ans += 1
        n_g = []
        for v in g:
            length = len(G[v])
            if not length:
                continue
            size[G[v][0]] -= 1
            if not size[G[v][0]]:
                n_g.append(G[v][0])
            if length == 2:
                size[G[v][1]] -= 1
                if not size[G[v][1]]:
                    n_g.append(G[v][1])
        g = n_g
    for s in size:
        if s != 0:
            print(-1)
            return
    print(ans)


def __starting_point():
    main()


__starting_point()
