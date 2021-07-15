n,m=map(int,input().split())
h=list(map(int,input().split()))
l=[1]*n
for i in range(m):
  a,b=map(int,input().split())
  if h[a-1]==h[b-1]:
    l[a-1]=0
    l[b-1]=0
  if h[a-1]>h[b-1]:
    l[b-1]=0
  if  h[a-1]<h[b-1]:
    l[a-1]=0
print(l.count(1))
