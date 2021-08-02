from sys import setrecursionlimit
import threading


length = 0
visited = None
g = None


def dfs(v, path_length, chance):
    nonlocal length
    visited.add(v)
    edges = 0
    for n in g[v]:
        if n not in visited:
            edges += 1
    for n in g[v]:
        if n not in visited:
            dfs(n, path_length + 1, chance * (1 / edges))
    if edges == 0:
        length += path_length * chance


def main():
    nonlocal visited, g
    vert = int(input())
    g = [[] for _ in range(vert + 1)]
    visited = set()
    for _ in range(vert - 1):
        a, b = list(map(int, input().split()))
        g[a].append(b)
        g[b].append(a)
    dfs(1, 0, 1)
    print(length)


def __starting_point():
    setrecursionlimit(10 ** 6)
    threading.stack_size(134217728)
    thread = threading.Thread(target=main)
    thread.start()


__starting_point()
