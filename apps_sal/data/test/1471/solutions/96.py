import sys
sys.setrecursionlimit(1<<30)

N = int(input())
def dfs(x):
    for y in Tree[x]:
        if Parent[x] != y:
            Parent[y] = x
            distance[y] += Web[min(x,y),max(x,y)]+distance[x]
            dfs(y)
Tree = [[] for i in range(N+1)]
Parent = [0]*(N+1)
Web = dict()
for i in range(N-1):
    a,b,w = map(int,input().split())
    Tree[a].append(b)
    Tree[b].append(a)
    Web[(min(a,b),max(a,b))] = w
distance = [0]*(N+1)
dfs(1)
for i in distance[1:]:
    if i%2 == 0:
        print(1)
    else:
        print(0)
