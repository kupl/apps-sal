# cook your dish here
n,m=map(int,input().split())
a=[int(x) for x in input().split()]
mh=min(a)
mp=max(a)
for i in range(m):
 b=int(input())
 if(b<=mp and b>=mh):
  print("Yes")
 else:
  print("No")
