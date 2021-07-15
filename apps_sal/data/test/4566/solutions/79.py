from collections import Counter

n,m=map(int,input().split())

l=[]
for i in range(m):
  lis=list(map(int,input().split()))
  l+=lis
  
l=Counter(l)

for i in range(1,n+1):
  print(l[i])
