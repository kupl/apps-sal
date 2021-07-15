# cook your dish here
import collections
n,m=map(int,input().split())
red=[]
blue=[]
for i in range(n):
    x,u=map(int,input().split())
    red.append(x*u)
for i in range(m):
    y,v=map(int,input().split())
    blue.append(y*v)
count=0
r=dict(collections.Counter(red))
b=dict(collections.Counter(blue))
for i in r:
    if i in b:
        count+= min(r[i],b[i])
print(count)

