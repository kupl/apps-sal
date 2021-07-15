n,x=map(int,input().split())
sum=0
s=1000
for i in range(n):
  m=int(input())
  sum+=m
  s=min(s,m)

y=x-(sum)
z=y//s
print(n+z)
