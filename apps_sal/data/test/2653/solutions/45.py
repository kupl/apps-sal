import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

# 遅延評価で加えてあげるだけ

N, Q = map(int, input().split())
AB = [[int(x) for x in input().split()] for _ in range(N - 1)]
PX = [[int(x) for x in input().split()] for _ in range(Q)]

graph = [[] for _ in range(N + 1)]
for a, b in AB:
    graph[a].append(b)
    graph[b].append(a)

value = [0] * (N + 1)
for p, x in PX:
    value[p] += x


def dfs(v, parent, add):
    value[v] += add
    for x in graph[v]:
        if x == parent:
            continue
        dfs(x, v, value[v])


dfs(1, 0, 0)

answer = ' '.join(map(str, value[1:]))
print(answer)
