from collections import deque
from sys import stdin
n=int(stdin.readline().strip())
s=list(map(int,stdin.readline().strip().split()))
s.sort()
a=deque()
a.append(s[-1])
flag=True
s.pop()
while len(s)>0:
    if flag:
        a.appendleft(s[-1])
    else:
        a.append(s[-1])
    flag= not flag
    s.pop()
flag=True
for i in range(n):

    if (a[(i-1)%n]+a[(i+1)%n])<=a[i]:
        flag=False
        break
if flag:
    print("YES")
    print(*a)
else:
    print("NO")
        

