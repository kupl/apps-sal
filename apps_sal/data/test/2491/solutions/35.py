import sys
input = sys.stdin.readline


def readlines(n):
    for _ in range(n):
        a, b, c = map(int, input().split())
        yield a, b, c


def main():
    n, m = map(int, input().split())
    edges = [(a - 1, b - 1, -c) for a, b, c in readlines(m)]
    costs = bellman_ford(0, edges, n)

    if costs == -1:
        print("inf")
    else:
        print(-costs[-1])


def bellman_ford(start, edges, n):
    inf = float("inf")
    costs = [inf] * n
    costs[start] = 0
    for i in range(n):
        for u, v, weight in edges:
            if costs[u] + weight < costs[v]:
                costs[v] = costs[u] + weight
                if i == n - 1 and v == n - 1:
                    return -1

    return costs


main()
