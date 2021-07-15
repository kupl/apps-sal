import sys
sys.setrecursionlimit(10**7)

def dfs(st, depth=0):
    dist[st] = depth
    for to, c in tree[st]:
        if dist[to]>=0:
            continue
        dfs(to, depth+c)


N = int(input())
tree = [[] for _ in range(N)]
dist = [-1]*N

for _ in range(N-1):
    a,b,c = map(int, input().split())
    tree[a-1].append((b-1, c))
    tree[b-1].append((a-1, c))

Q, K = map(int, input().split())
dfs(K-1, 0)
# print(dist)
# print(tree)
for _ in range(Q):
    x, y = map(int, input().split())
    print(dist[x-1]+dist[y-1])
