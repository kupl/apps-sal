n=int(input())
l=list(map(int,input().split()))
x=[0]*n
for i in range(n):
  x[l[i]-1]+=1
d=0
for i in range(n):
  d=d+x[i]*(x[i]-1)//2

for i in range(n):
  b=d-(x[l[i]-1]-1)
  print(b)
    

