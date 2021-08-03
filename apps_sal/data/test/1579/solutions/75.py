import sys
read = sys.stdin.buffer.read
readlines = sys.stdin.buffer.readlines
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)


def main():
    OFS = 100005
    N = int(input())
    G = [[] for _ in [0] * OFS * 2]
    for line in readlines():
        x, y = map(int, line.split())
        y += OFS
        G[x].append(y)
        G[y].append(x)

    def dfs(v):
        if v < OFS:
            counter[0] += 1
        else:
            counter[1] += 1

        for u in G[v]:
            if visited[u]:
                continue
            visited[u] = 1
            dfs(u)

    visited = [0] * OFS * 2
    ans = 0
    for i in range(OFS):
        if visited[i]:
            continue
        counter = [0] * 2
        visited[i] = 1
        dfs(i)
        ans += counter[0] * counter[1]

    print(ans - N)


def __starting_point():
    main()


__starting_point()
