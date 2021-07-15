n,k=map(int, input().split())
vis = [0] * 17
for _ in range(n):
	a = list(map(int, input().split()))
	vis[sum(a[i]*(1<<i) for i in range(k))] = 1
flag=0
for i in range(16):
	for j in range(16):
		if i&j==0 and vis[i] and vis[j]: flag=1
print("YES" if flag else "NO")
