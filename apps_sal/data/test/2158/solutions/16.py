n = int(input())
al = [[] for j in range(n)]
for i in range(n - 1):
    a, b, c = list(map(int, input().split()))
    al[a].append([b, c])
    al[b].append([a, c])

mc = 0
va = [0] * (n)
ca = [0] * (n)


def dfs(n, c):
    va[n] = 1
    ca[n] = ca[n] + c

    for e in al[n]:
        p = e[0]
        q = e[1] + ca[n]
        if(va[p] == 0):
            dfs(p, q)


dfs(0, 0)
print(max(ca))

'''
mc = 0
cost = 0
visited = [False] * n
def DFS(num,visited,cost):
    nonlocal mc
    if cost > mc:
        mc = cost
    visited[num] = True
    for i in range(len(li[num])):
        if not visited[li[num][i][0]]:
            DFS(li[num][i][0],visited,cost+li[num][i][1])
DFS(0,visited,0)
print(mc)'''
