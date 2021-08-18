import sys
from collections import defaultdict


def main():
    n, m = [int(x) for x in sys.stdin.readline().split(" ")]
    graph = defaultdict(list)
    for _ in range(m):
        u, v = [int(x) for x in sys.stdin.readline().split(" ")]
        graph[u].append(v)
        graph[v].append(u)
    maxB = -1
    count = 0
    visited = [False for v in range(0, n + 1)]
    stack = []
    for i in range(1, n + 1):
        if visited[i]:
            continue
        if i < maxB:
            count += 1
        stack = [i]
        while (len(stack) > 0):
            u = stack.pop()
            for v in graph[u]:
                if v > maxB:
                    maxB = v
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
    return(count)


print(main())
