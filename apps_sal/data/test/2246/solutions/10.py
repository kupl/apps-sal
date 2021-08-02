"""
    Author      : Arif Ahmad
    Date        : 
    Algo        : 
    Difficulty  : 
"""
from sys import stdin, stdout


def main():
    n = int(stdin.readline().strip())
    g = [[] for i in range(n + 1)]
    for _ in range(n - 1):
        u, v = [int(_) for _ in stdin.readline().strip().split()]
        g[u].append(v)
        g[v].append(u)

    visited = [False for i in range(n + 1)]
    paths = []

    # iterative DFS
    stack = [(1, 0, 1)]
    while len(stack):
        u, plen, prb = stack.pop()

        visited[u] = True
        nBranch = 0
        for v in g[u]:
            if not visited[v]: nBranch += 1

        if nBranch > 0:
            probability = prb * (1 / nBranch)
            for v in g[u]:
                if not visited[v]:
                    stack.append((v, plen + 1, probability))

        if nBranch == 0:
            paths.append(plen * prb)

    ans = sum(paths)
    stdout.write(str(ans) + '\n')


def __starting_point():
    main()


__starting_point()
