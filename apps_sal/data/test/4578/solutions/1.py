n,x=map(int,input().split())
a=[]
for i in range(n):
  m=int(input())
  a.append(m)
  x-=m
while x>=min(a):
  x-=min(a)
  n+=1
print(n)
