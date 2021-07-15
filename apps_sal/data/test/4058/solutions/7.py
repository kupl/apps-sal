def mi():
	return list(map(int, input().split()))

'''
6 2
0 1 1 0 0 1
'''
n,r = mi()
a = list(mi())
def fun(n,a,r):
	vis = [0]*n
	i = 0
	cnt = 0
	for j in range(min(r,n)):
		if a[j]==1:
			i = j
	while i<n:
		#print (i)
		if vis[i]==1 and vis[min(n,end+r)-1]==1:
			break
		if a[i]==1:
			cnt+=1
			j = max(0,i-(r-1))
			end = min(n, i+r)
			next = 0
			while j<end:
				vis[j]=1
				j+=1
			next = 0
			for k in range(i+1, min(n,end+r)):
				if a[k]==1:
					next = k
			if next:
				i = next
				continue
		i+=1
	#print (a)
	#print (vis)
	if 0 in vis:
		return -1
	else:
		return cnt
print(max(fun(n,a,r), fun(n,a[::-1],r)))

