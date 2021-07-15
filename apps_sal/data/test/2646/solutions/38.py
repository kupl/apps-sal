n,m = map(int,input().split())
r = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    r[a].append(b)
    r[b].append(a)

import collections
q = collections.deque()

sigh = [-1] * (n+1)

for i in r[1]:
    q.append((1,i))
    
while q:
    xy = q.popleft()
    x = xy[0]
    y = xy[1]
    
    if sigh[y] == -1:
        sigh[y] = x
        
        for i in r[y]:
            q.append([y,i])
            
print("Yes")
print(*sigh[2:],sep="\n")
