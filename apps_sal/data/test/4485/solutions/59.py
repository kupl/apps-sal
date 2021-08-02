N, M = map(int, input().split())

ki = [list() for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ki[a].append(b)

K = [-1] * N


def dfs(now, time):
    K[now] = time
    for i in ki[now]:
        time += 1
        dfs(i, time)
        time -= 1


dfs(0, 0)
print('POSSIBLE' if K[N - 1] == 2 else 'IMPOSSIBLE')
