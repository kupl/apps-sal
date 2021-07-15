N,M = map(int,input().split())
s = [[] for i in range(N)]
m = []
for i in range(M):
    a,b = map(int,input().split())
    s[a-1].append(b)
    s[b-1].append(a)
    m.append([a,b])
ans = 0
from collections import deque
import copy
d = deque()
for i in range(M):
    n = [0] * N
    a = m[i][0]
    b = m[i][1]
    c = s[a-1].copy()
    c.remove(b)
    d.append(c)
    n[a-1] = 1
    while len(d) > 0:
        e = d.popleft()
        for j in e:
            if n[j-1] == 0:
                n[j-1] = 1
                d.append(s[j-1])
    if 0 in n:
        ans += 1
print(ans)
