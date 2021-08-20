import sys
read = sys.stdin.read
sys.setrecursionlimit(10 ** 7)


def main():

    def dfs(v, s):
        if added[v]:
            pass
        else:
            scores[v] += s
            added[v] = 1
            for nextv in gg[v]:
                dfs(nextv, scores[v])
    data = tuple(map(int, read().split()))
    (n, q) = (data[0], data[1])
    gg = {i: set() for i in range(1, n + 1)}
    for (i1, v1) in zip(data[2:n * 2:2], data[3:n * 2:2]):
        gg[v1].add(i1)
        gg[i1].add(v1)
    scores = [0] * (n + 1)
    for (j1, v1) in zip(data[n * 2::2], data[n * 2 + 1::2]):
        scores[j1] += v1
    added = [0] * (n + 1)
    dfs(1, 0)
    print(*scores[1:], sep=' ')


def __starting_point():
    main()


__starting_point()
