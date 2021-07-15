n,k=map(int,input().split())
r=list(map(int,input().split()))
dist=[]
ans=[0]*(k+1)#precomp
for i in range(n):
	if i == 0 or r[i] != r[i - 1]:
		dist.append(r[i])
# dist = distinct
for i in range(len(dist)):
	if 0 < i < len(dist) - 1 and dist[i - 1] == dist[i + 1]:
		ans[dist[i]] += 2 # removing dist[i] subtracts 2
	else:
		ans[dist[i]] += 1
u, v = -1, -1
for k in range(1, k + 1):
	if ans[k] > u: u, v = ans[k], k
print (v)
