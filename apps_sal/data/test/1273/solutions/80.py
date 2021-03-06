import sys
sys.setrecursionlimit(200000)


def solve(N: int, a: 'List[int]', b: 'List[int]'):
    from itertools import count
    edges = [[] for _ in range(N)]
    for (i, (aa, bb)) in enumerate(zip(a, b)):
        edges[aa - 1].append((bb - 1, i))
        edges[bb - 1].append((aa - 1, i))
    ans = [None] * (N - 1)
    visited = set()

    def dfs(n, c):
        if n in visited:
            return
        visited.add(n)
        for ((nn, i), cc) in zip(filter(lambda x: x[0] not in visited, edges[n]), filter(lambda y: y != c, count(1))):
            ans[i] = cc
            dfs(nn, cc)
    dfs(0, None)
    return [max(ans)] + ans


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    a = [int()] * (N - 1)
    b = [int()] * (N - 1)
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    print(*solve(N, a, b), sep='\n')


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
