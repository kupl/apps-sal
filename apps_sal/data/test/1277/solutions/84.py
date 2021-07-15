from collections import deque
n , u , v = map(int,input().split())
u -= 1
v -= 1
route = [[] for i in range(n)]
for i in range(n-1):
    a , b = map(lambda x:int(x)-1,input().split())
    route[a].append(b)
    route[b].append(a)

takyori = [-1 for i in range(n)]
takyori[u] = 0
d = deque()
d.append(u)
while d:
    now = d.popleft()
    for i in route[now]:
        if takyori[i] == -1:
            takyori[i] = takyori[now] + 1
            d.append(i)

aokyori = [-1 for i in range(n)]
aokyori[v] = 0
d = deque()
d.append(v)
while d:
    now = d.popleft()
    for i in route[now]:
        if aokyori[i] == -1:
            aokyori[i] = aokyori[now] + 1
            d.append(i)
ans = 0
for i in range(n):
    if takyori[i] <= aokyori[i]:
        ans = max(ans,aokyori[i]-1)
print(ans)
