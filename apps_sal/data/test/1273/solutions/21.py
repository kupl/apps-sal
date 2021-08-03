import sys

sys.setrecursionlimit(100000)


def main():
    n = int(input())
    G = [[] for _ in range(n)]
    ID = [dict() for _ in range(n)]
    for i in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        G[a].append(b)
        G[b].append(a)
        ID[a][b] = i
        ID[b][a] = i
    m = max(len(g) for g in G)
    ans = [0] * (n - 1)

    def bfs(a, pre=-1, pre_c=-1):
        color = 1
        for b in G[a]:
            if b == pre:
                continue
            if color == pre_c:
                color += 1
            ans[ID[a][b]] = color
            bfs(b, a, color)
            color += 1

    bfs(0)
    print(m)
    [print(a) for a in ans]


def __starting_point():
    main()


__starting_point()
