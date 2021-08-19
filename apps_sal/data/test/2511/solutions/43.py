import sys
sys.setrecursionlimit(10 ** 9)


def dfs(num):
    temp = K - len(way[num])
    for w in way[num]:
        if visited[w] == -1:
            visited[w] = temp
            temp += 1
            dfs(w)
    return


(N, K) = list(map(int, input().split()))
mod = 10 ** 9 + 7
visited = [-1] * N
way = [[] for i in range(N)]
for _ in range(N - 1):
    (a, b) = list(map(int, input().split()))
    way[a - 1].append(b - 1)
    way[b - 1].append(a - 1)
color = []
visited[0] = K
dfs(0)
ans = 1
for item in visited:
    ans *= item
    ans %= mod
print(ans)
