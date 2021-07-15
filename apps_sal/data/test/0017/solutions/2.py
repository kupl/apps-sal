n,k,t = map(int,input().split())
if(t <= k):
	print(t)
elif(t >= n+1):
	print(n+k-t)
else:
	print(k)
