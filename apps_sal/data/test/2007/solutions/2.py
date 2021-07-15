from sys import stdin
input=lambda : stdin.readline().strip()
from math import ceil,sqrt,factorial,gcd
from collections import deque
from bisect import bisect_left
n,m=map(int,input().split())
l=list(input())
degree=[0 for i in range(n)]
graph={i:[] for i in range(n)}
for i in range(m):
	a,b=map(int,input().split())
	a-=1
	b-=1
	graph[a].append(b)
	degree[b]+=1
q=deque()
for i in range(n):
	if degree[i]==0:
		q.append(i)
count=0
ans=0
# print(degree)
dp=[[0 for i in range(26)] for i in range(n)]
while count<n and q:
	x=q.popleft()
	count+=1
	# print(ord(l[x])-97)
	dp[x][ord(l[x])-97]+=1
	for i in graph[x]:
		for j in range(26):
			dp[i][j]=max(dp[i][j],dp[x][j])
		degree[i]-=1
		if degree[i]==0:
			q.append(i)
# print(degree)
if count!=n:
	print(-1)
else:
	ans=0
	for i in range(n):
		ans=max(ans,max(dp[i]))
	print(ans)
