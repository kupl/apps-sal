import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def dfs(now):
    seen[now] = True
    for next in branch[now]:
        if seen[next] is False:
            score[next] += score[now]
            dfs(next)


N, Q = list(map(int, input().split()))
branch = [set() for _ in range(N)]
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    branch[a - 1].add(b - 1)
    branch[b - 1].add(a - 1)
score = [0] * N
for _ in range(Q):
    p, x = list(map(int, input().split()))
    score[p - 1] += x

seen = [False] * N
for i in range(N):
    if seen[i] is False:
        dfs(i)

print((*score))
