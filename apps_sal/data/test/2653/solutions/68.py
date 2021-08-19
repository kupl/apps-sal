import sys
sys.setrecursionlimit(10 ** 7)
(N, Q) = [int(n) for n in input().split()]
tree_list = [[] for _ in range(N)]
for i in range(N - 1):
    (a, b) = [int(n) - 1 for n in input().split()]
    tree_list[a].append(b)
    tree_list[b].append(a)
score_list = [0] * N
for j in range(Q):
    (p, x) = [int(n) for n in input().split()]
    score_list[p - 1] += x
reached = [False] * N


def dfs(v):
    reached[v] = True
    for next_v in tree_list[v]:
        if reached[next_v] == True:
            continue
        score_list[next_v] += score_list[v]
        dfs(next_v)


dfs(0)
print(*score_list)
