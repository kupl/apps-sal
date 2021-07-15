"""
NTC here
"""
from sys import setcheckinterval,stdin
setcheckinterval(1000)

from collections import defaultdict

iin=lambda :int(stdin.readline())
lin=lambda :list(map(int,stdin.readline().split()))

n=iin()
a=input()
b=input()
l=defaultdict(list)
cntl=defaultdict(int)
for i in range(n):
    l[a[i]].append(i+1)
cl=len(l['?'])
left=defaultdict(list)
ans=[]
for i in range(n):
    if b[i]=='?':left['?'].append(i+1);continue
    if b[i] in l:
        if l[b[i]]:
            ans.append((l[b[i]].pop(),i+1))
        else:
            left[b[i]].append(i+1)
    else:
        left[b[i]].append(i+1)
cr=len(left['?'])
if cl!=0:
    for i in left:
        if i=='?':continue
        if cl<=0:break
        while left[i] and cl>0:
            ans.append((l['?'].pop(),left[i].pop()))
            cl-=1
if cr!=0:
    for i in l:
        if l[i]:
            while l[i] and cr>0:
                ans.append((l[i].pop(),left['?'].pop()))
                cr-=1
print(len(ans))
for i,j in ans:
    print(i,j)



