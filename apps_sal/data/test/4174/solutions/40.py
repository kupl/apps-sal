n,x=map(int, input().split())
l=list(map(int, input().split()))
d=0
count=0
for i in range(n):
  d+=l[i]
  if d>x:
    print(i+1)
    break
  if i==n-1 and d<=x:
    print(n+1)
