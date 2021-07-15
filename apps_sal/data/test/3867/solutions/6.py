from sys import stdin
from collections import deque
n=int(stdin.readline())
g=dict()
for i in range(n-1):
    a,b=list(map(int,stdin.readline().strip().split()))
    g.setdefault(a, set()).add(b)
    g.setdefault(b, set()).add(a)
a=[int(x) for x in stdin.readline().strip().split()]
ans = True
if n > 1 and a[0] == 1:
    q=deque()
    m=[0]*(n+1)
    q.append(1)
    m[1]=1
    right=1
    while len(q) > 0 and ans:
        first = q.popleft()
        cnt = 0
        for v in g[first]:
            if m[v] == 0:
                cnt += 1
        for i in range(right, right+cnt):
            if m[a[i]] == 0 and a[i] in g[first]:
                m[a[i]] = 1
                q.append(a[i])
            else:
                ans = False
                break
        right += cnt
else:
    ans = a[0] == 1
if ans:
    print("Yes")
else:
    print("No")

