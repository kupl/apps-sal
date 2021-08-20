import sys
sys.setrecursionlimit(1 << 30)
(N, Q) = map(int, input().split())


def dfs(x, score):
    for y in Tree[x]:
        if Parent[x] != y:
            Parent[y] = x
            score[y] += score[x]
            dfs(y, score)


Tree = [[] for i in range(N + 1)]
Parent = [0] * (N + 1)
for i in range(N - 1):
    (a, b) = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)
score = [0] * (N + 1)
for j in range(Q):
    (p, x) = map(int, input().split())
    score[p] += x
dfs(1, score)
print(*score[1:], end='\t')
