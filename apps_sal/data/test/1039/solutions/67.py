import sys
sys.setrecursionlimit(10**9)

n = int(input())

tree = [[] for i in range(n+1)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

q,k = map(int,input().split())

distance = [-1 for i in range(n+1)]

#再帰でkから各頂点までの距離を求める
def dfs(now, pre, c):
    distance[now] = c
    for nxt, val in tree[now]:
        if nxt == pre:
            continue
        dfs(nxt, now, c+val)

dfs(k, -1, 0)

for i in range(q):
    x,y = map(int,input().split())
    print(distance[x] + distance[y])
