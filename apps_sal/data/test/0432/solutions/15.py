# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/10/18

"""

N = int(input())
C = [0] + [int(x) for x in input().split()]
A = [0] + [int(x) for x in input().split()]


ans = 0
vis = [False] * (N+1)
for i in range(1, N+1):
    if vis[i]:
        continue
    
    circle = []
    u = i
    while not vis[u]:
        circle.append(u)
        vis[u] = True
        u = A[u]
    
    if u in circle:
        ans += min([C[j] for j in circle[circle.index(u):]])

print(ans)
