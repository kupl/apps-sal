import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def main():
    N, K = NMI()
    edges = [NLI() for _ in range(N - 1)]
    tree = make_adjlist_nond(N, edges)
    stack = deque()
    stack.append(1)
    ans = K
    seen = [False] * (N + 1)
    while stack:
        now = stack.pop()
        seen[now] = True
        tmp = K - 2
        if now == 1:
            tmp += 1
        cnt = 0
        for i, goto in enumerate(tree[now]):
            if seen[goto]:
                cnt += 1
                continue
            ans = ans * (tmp - i + cnt) % MOD
            stack.append(goto)

    print(ans % MOD)


def __starting_point():
    main()


__starting_point()
