# cook your dish here
n=int(input())
l=list(map(int,input().split()))
l.append(0)
prev=0
curr=0
u=0
for i in range(n+1):
 if l[i]==0:
  prev=curr
  curr=i 
  d=abs(curr-prev)
  curr=curr+1
  
  u=max(u,d)
print(u)
