# 解説AC
# 二部グラフでないグラフの性質や，パスの長さを考察する

def main():
    N, M = (int(i) for i in input().split())

    par = [i for i in range(N)]
    size = [1 for i in range(N)]

    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            size[x] = size[par[x]]
            return par[x]

    def same(x, y):
        return find(x) == find(y)

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        size[x] += size[y]
        par[y] = x

    def get_size(x):
        return size[find(x)]

    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = (int(i) for i in input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
        union(a-1, b-1)

    S = [False]*4
    for i in range(N):
        S[min(3, get_size(i))] = True
        if S[3]:
            break
    t = 0
    if S[3]:
        t = 1
    elif S[2]:
        t = 2
    else:
        t = 3

    color = [-1]*N

    def dfs(s):
        stack = [s]
        color[s] = 0
        b = 1
        w = 0
        while stack:
            v = stack.pop()
            for u in G[v]:
                if color[u] != -1:
                    if color[u] == color[v]:
                        return False, b*w
                    continue
                color[u] = color[v] ^ 1
                if color[u] == 0:
                    b += 1
                else:
                    w += 1
                stack.append(u)
        return True, b*(b-1)//2 + w*(w-1)//2

    is_bipartite, _ = dfs(0)
    if is_bipartite:
        w = 0
        if t == 3:
            w = N*(N-1)*(N-2)//3//2
        elif t == 2:
            used = [False]*N
            for i in range(N):
                if not used[find(i)] and get_size(i) == 2:
                    w += (N-2)
                    used[find(i)] = True
        elif t == 1:
            used = [False]*N
            color = [-1]*N
            for i in range(N):
                if not used[find(i)] and get_size(i) >= 3:
                    _, ways = dfs(i)
                    w += ways
                    used[find(i)] = True
        print(t, w)
    else:
        print(0, 1)


def __starting_point():
    main()

__starting_point()
