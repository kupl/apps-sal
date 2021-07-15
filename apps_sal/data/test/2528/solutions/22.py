# cook your dish here
n=int(input())
l=list(map(int,input().split()))
m=0
c=0
for i in range(n):
 if l[i]>0:
  c=c+1
 else:
  m=max(m,c)
  c=0
m=max(m,c)
print(m)

