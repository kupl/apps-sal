import sys
(N, u, v) = list(map(int, input().split()))
sys.setrecursionlimit(10 ** 6)
T = [[] for _ in range(N)]
for i in range(N - 1):
    (a, b) = list(map(int, input().split()))
    T[a - 1].append(b - 1)
    T[b - 1].append(a - 1)


def dfs(start):
    tolist = T[start]
    nowd = done[start]
    for next_n in tolist:
        if done[next_n] == -1:
            done[next_n] = nowd + 1
            dfs(next_n)


done = [-1] * N
done[u - 1] = 0
dfs(u - 1)
dtaka = done.copy()
done = [-1] * N
done[v - 1] = 0
dfs(v - 1)
dao = done.copy()
ans = 0
for i in range(N):
    t = dtaka[i]
    a = dao[i]
    if a > t:
        ans = max(ans, a)
print(ans - 1)
