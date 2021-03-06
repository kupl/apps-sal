import os
import sys
from collections import deque


def main():
    (N, M) = list(map(int, input().split()))
    path = [[] for _ in range(N + 1)]
    for _ in range(M):
        (a, b) = list(map(int, input().split()))
        path[a].append(b)
        path[b].append(a)
    Q = deque(path[1])
    flag = False
    while Q and flag is False:
        u = Q.popleft()
        for v in path[u]:
            if v == N:
                flag = True
    if flag:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


def __starting_point():
    main()


__starting_point()
