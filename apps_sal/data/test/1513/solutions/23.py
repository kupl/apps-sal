import sys
import math
input = sys.stdin.readline

n,m,k=map(int,input().split())

l=list(map(int,input().split()))

dist=[]

for i in range(n-1):
	dist.append(l[i+1]-l[i])

dist.sort()

ans=0
for i in range(n-k):
	ans+=dist[i]

ans+=k

print(ans)
