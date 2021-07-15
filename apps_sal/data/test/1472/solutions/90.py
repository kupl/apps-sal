n,x,y=map(int,input().split())
x,y=x-1,y-1
c=[0 for i in range(n-1)]

for i in range(n):
  for j in range(i+1,n):
    l=min(j-i,abs(i-x)+abs(j-y)+1)
    c[l-1]+=1

for i in range(n-1):
  print(c[i])
