def resolve():

    def dfs(v):
        dist = [-1] * N
        stack = [v]
        dist[v] = 0
        while stack:
            v = stack.pop()
            for to in G[v]:
                if dist[to] != -1:
                    continue
                dist[to] = dist[v] + 1
                stack.append(to)
        return dist
    (N, taka, aoki) = map(int, input().split())
    taka -= 1
    aoki -= 1
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        (a, b) = map(lambda x: int(x) - 1, input().split())
        G[a].append(b)
        G[b].append(a)
    dist_Tk = dfs(taka)
    dist_Ao = dfs(aoki)
    ans = 0
    for i in range(N):
        if dist_Tk[i] < dist_Ao[i]:
            ans = max(ans, dist_Ao[i] - 1)
    print(ans)


def __starting_point():
    resolve()


__starting_point()
