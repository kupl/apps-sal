import sys
import math
input = sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
cur=[0]*n
tot=sum(arr)
dic={}
q=int(input())
for i in range(q):
	s,t,u=map(int,input().split())
	# print(cur)
	if (s,t) in dic:
		# print("yo")
		v=dic[(s,t)]
		del dic[(s,t)]
		if cur[v-1]<=arr[v-1]:
			# print("x")
			tot+=1
		cur[v-1]-=1
	if u>0:
		dic[(s,t)]=u
		if cur[u-1]<arr[u-1]:
			tot-=1
		cur[u-1]+=1
	# print(dic)
	print(tot)
