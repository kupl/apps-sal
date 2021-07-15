N,M = map(int,input().split())
t = [[i+1] for i in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    t[A-1].append(B)
    t[B-1].append(A)
from collections import deque
d = deque()
ans = [-1]*(N)
d.append(t[0])
while len(d) > 0:
    z = d.popleft()
    x = z[0]
    for i in range(1,len(z)):
        if ans[z[i]-1] == -1:
            ans[z[i]-1] = x
            d.append(t[z[i]-1])
print("Yes")
for i in range(1,len(ans)):
    print(ans[i])
