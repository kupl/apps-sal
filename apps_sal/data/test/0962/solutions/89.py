from sys import setrecursionlimit
setrecursionlimit(10000)
N, M = list(map(int, input().split()))
table = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    table[a-1].append(b-1)

visit = [False] * N
visit2 = [False] * N
g = []


def dfs(v):
    g.append(v)
    if visit[v]:
        return True
    visit[v] = True
    visit2[v] = True
    for u in table[v]:
        if dfs(u):
            return True
    g.pop()
    visit[v] = False
    return False


for i in range(N):
    g = []
    if not visit2[i]:
        if dfs(i):
            break
else:
    print((-1))
    return
print((0))
# ans = [v+1 for v in g[g.index(g[-1]):-1]]
# print(len(ans))
# print(*ans, sep="\n")

