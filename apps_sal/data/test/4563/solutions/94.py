n=int(input())
x,y=map(int,input().split())
z=x+y
for i in range(n-1):
  a,b=map(int,input().split())
  k=max((x-1)//a,(y-1)//b)+1
  x=k*a
  y=k*b
print(x+y)
