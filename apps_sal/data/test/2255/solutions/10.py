import sys
import heapq
#sys.setrecursionlimit(200000)
input = sys.stdin.readline
n,m = map(int,input().split())
g = [[] for i in range(n)]
for i in range(m):
        a,b = map(int,input().split())
        a-=1;b-=1
        g[a].append(b)
        g[b].append(a)
que = [0]
heapq.heapify(que)
ans = []
used = [0]*n
for i in range(n):
        a = heapq.heappop(que)
        while used[a] == 1:
             a = heapq.heappop(que)   
        used[a] = 1
        ans.append(a+1)
        for j in g[a]:
                if used[j] == 0:
                        heapq.heappush(que,j)
print(*ans)
