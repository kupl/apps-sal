import math
from collections import defaultdict
import sys


def main():
    (n, q) = list(map(int, input().split()))
    children = [[] for _ in range(n)]
    parent = list(map(int, input().split()))
    for i in range(n - 1):
        children[parent[i] - 1].append(i + 1)
    d = []
    cnt = [1] * n
    stack = [0]

    def dfs():
        while stack:
            node = stack.pop()
            d.append(node)
            for i in range(len(children[node]) - 1, -1, -1):
                stack.append(children[node][i])
    dfs()
    for i in range(n - 1, -1, -1):
        total = 0
        for child in children[i]:
            total += cnt[child]
        cnt[i] += total
    indexof = [-1] * n
    for (i, val) in enumerate(d):
        indexof[val] = i
    for _ in range(q):
        (u, k) = list(map(int, input().split()))
        index = indexof[u - 1]
        pos = index + k - 1
        if k > cnt[u - 1]:
            print(-1)
        else:
            print(d[pos] + 1)


def __starting_point():
    main()


__starting_point()
