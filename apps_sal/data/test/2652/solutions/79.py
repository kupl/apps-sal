from heapq import heappush, heappop, heapify
import math
import sys
sys.setrecursionlimit(2147483647)
input = sys.stdin.readline


def solve(n, nodes):
    xsort_nodes = sorted(nodes, key=lambda n: n[1])
    ysort_nodes = sorted(nodes, key=lambda n: n[2])
    edges = [[] for _ in range(n)]
    for i in range(n - 1):
        prev_node = xsort_nodes[i]
        post_node = xsort_nodes[i + 1]
        edges[prev_node[0]].append((abs(prev_node[1] - post_node[1]), post_node[0]))
    for i in range(n - 1):
        prev_node = ysort_nodes[i]
        post_node = ysort_nodes[i + 1]
        edges[prev_node[0]].append((abs(prev_node[2] - post_node[2]), post_node[0]))
    for i in range(1, n):
        prev_node = xsort_nodes[i - 1]
        post_node = xsort_nodes[i]
        edges[post_node[0]].append((abs(prev_node[1] - post_node[1]), prev_node[0]))
    for i in range(1, n):
        prev_node = ysort_nodes[i - 1]
        post_node = ysort_nodes[i]
        edges[post_node[0]].append((abs(prev_node[2] - post_node[2]), prev_node[0]))
    tree = [0] * n
    tree[0] = 1
    distance = 0
    current_edges = [*edges[0]]
    heapify(current_edges)
    while len(current_edges):
        (d, x) = heappop(current_edges)
        if tree[x]:
            continue
        distance += d
        tree[x] = 1
        for edge in edges[x]:
            heappush(current_edges, edge)
    return distance


def main():
    n = int(input())
    nodes = []
    for i in range(n):
        (x, y) = map(int, input().split(' '))
        nodes.append((i, x, y))
    ans = solve(n, nodes)
    print(ans)


def __starting_point():
    main()


__starting_point()
