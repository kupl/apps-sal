import sys

x,n=map(int,input().split())
p=list(map(int,input().split()))
p.sort()

if n==0:
    print(x)
    return

if x not in p:
    print(x)
    return
    
q=list(i for i in range(p[0]-1,p[-1]+2))

for i in p:
    q.remove(i)

ans=[]
c=x+n
for i in q:
    if c>abs(x-i):
        c=abs(x-i)
        ans.clear()
        ans.append(i)
    if c==abs(x-i):
        ans.append(i)

print(min(ans))
