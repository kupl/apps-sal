"""
    # recursive DFS gives RTE, implement iterative DFS
    Author      : Arif Ahmad
    Date        : 
    Algo        : 
    Difficulty  : 
"""
from sys import stdin, stdout, setrecursionlimit
import threading


g = None
visited = None
paths = None


def dfs(u, plen, prb):
    nonlocal visited, paths

    visited[u] = True

    nBranch = 0
    for v in g[u]:
        if not visited[v]:
            nBranch += 1

    if nBranch > 0:
        probability = prb * (1 / nBranch)
        for v in g[u]:
            #print(prb, nBranch)
            if not visited[v]:
                dfs(v, plen + 1, probability)

    if nBranch == 0:
        paths.append(plen * prb)


def main():
    nonlocal g, visited, paths

    n = int(stdin.readline().strip())
    g = [[] for i in range(n + 1)]
    for _ in range(n - 1):
        u, v = [int(_) for _ in stdin.readline().strip().split()]
        g[u].append(v)
        g[v].append(u)

    visited = [False for i in range(n + 1)]
    paths = []
    # setrecursionlimit(n+10)
    dfs(1, 0, 1)

    ans = sum(paths)
    stdout.write(str(ans) + '\n')


def __starting_point():
    setrecursionlimit(10**6)
    threading.stack_size(134217728)
    thread = threading.Thread(target=main)
    thread.start()


__starting_point()
