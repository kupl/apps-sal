import sys
from copy import deepcopy as copy
from collections import deque
input = sys.stdin.readline


def main():
    (n, m) = list(map(int, input().split()))
    tree = [[] for _ in range(n)]
    edge = dict()
    for i in range(m):
        (a, b) = list(map(int, input().split()))
        tree[a - 1].append(b - 1)
        edge[a - 1, b - 1] = i + 1
    ans = 0
    for i in range(n):
        not_yet = deque([i])
        already = [False] * n
        dist = [0] * n
        par = [0] * n
        already[i] = True
        sub = []
        while not_yet:
            key = not_yet.popleft()
            for v in tree[key]:
                if already[v]:
                    if v == i:
                        sub = [key + 1]
                        now = key
                        while now != i:
                            sub.append(par[now] + 1)
                            now = par[now]
                        break
                    continue
                not_yet.append(v)
                already[v] = True
                dist[v] = dist[key] + 1
                par[v] = key
            if sub:
                break
        if sub:
            if ans:
                if len(ans) > len(sub):
                    ans = copy(sub)
            else:
                ans = copy(sub)
    if ans:
        print(len(ans))
        for a in ans:
            print(a)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
