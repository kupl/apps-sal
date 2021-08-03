from sys import setrecursionlimit

setrecursionlimit(200000)


def main():
    n, m = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    avail = [True] * (n + 1)
    for _ in range(m):
        x, y = list(map(int, input().split()))
        graph[x].append(y)
        graph[y].append(x)

    def dfs(x, parent):
        if avail[x]:
            avail[x] = False
            res = True
            for y in graph[x]:
                if parent != y:
                    res = res and dfs(y, x)
            return res
        else:
            return False

    res = 0
    for j in range(1, n + 1):
        if avail[j]:
            if dfs(j, 0):
                res += 1
    print(res)


def __starting_point():
    main()


__starting_point()
