n,q = list(map(int,input().split()))
s = input()

d = [0]*100100
e = [0]*100100

for i in range(0,n-1):
	if s[i] == 'A' and s[i+1]=='C':
		d[i+1]=1

for i in range(0,n+1):
	d[i+1] += d[i]

for i in range(0,q):
	l,r = list(map(int,input().split()))
	l-=1
	lefNum = d[l]
	#if l > 0 and s[l-1] == 'A' and s[l] == 'C':
	#	lefNum-=1

	rigNum = d[r]
	if r < n and s[r-1] == 'A' and s[r] =='C':
		rigNum-=1
	#r-=1
	ans = rigNum - lefNum
	#print(l,r,ans)
	print(ans)

#for i in range(0,n):
#	print(i,d[i])
#	print(d[r]-d[l])

