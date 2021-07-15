from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))

d=defaultdict(int)
sm=0
for i in range(n):
  d[i+a[i]]+=1
  sm+=d[i-a[i]]
print(sm)

