import sys
from collections import deque
input = sys.stdin.readline


def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        (u, v, w) = list(map(int, input().split()))
        u -= 1
        v -= 1
        G[u].append((v, w))
        G[v].append((u, w))
    ans = [-1] * N
    ans[0] = 0
    stack = deque([(-1, 0)])
    while stack:
        (p, u) = stack.pop()
        for (v, w) in G[u]:
            if v == p:
                continue
            if w % 2 == 0:
                ans[v] = ans[u]
            else:
                ans[v] = (ans[u] + 1) % 2
            stack.append((u, v))
    print('\n'.join(map(str, ans)))


def __starting_point():
    main()


__starting_point()
