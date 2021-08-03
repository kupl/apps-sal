import queue

import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
S = set(range(N))

to = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    to[a].append(b)

visit = [0] * N


def DFS(p, n):
    if visit[p] != 0:
        return visit[p]
    else:
        visit[p] = n + 1
        for i in to[p]:
            r = DFS(i, n + 1)
            if r > 0:
                return r
        visit[p] = -1
        return -1


for i in range(N):
    r = DFS(i, 0)
    if r > 0:
        for j in range(N):
            if visit[j] < r:
                S.discard(j)
        for j in range(N):
            if j in S:
                for k in to[j]:
                    if k in S:
                        if visit[k] < visit[j]:
                            for l in range(N):
                                if visit[l] < visit[k] or visit[l] > visit[j]:
                                    S.discard(l)
                        else:
                            for l in range(N):
                                if visit[l] > visit[j] and visit[l] < visit[k]:
                                    S.discard(l)
        print(len(S))
        for j in list(S):
            print(j + 1)
        break
    if i == N - 1:
        print(-1)
