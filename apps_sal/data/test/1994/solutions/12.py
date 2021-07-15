def zeta(s):
	n = len(s)
	z = [0]*n
	l,r = 0,0
	for i in range(1,n):
		if(i<=r): z[i] = min(r-i+1,z[i-l])
		while(i+z[i]<n and s[z[i]]==s[i+z[i]]):
			z[i]+=1
		if(i+z[i]-1>r):
			l=i
			r = i+z[i]-1
	return z
s = input()
n = len(s)
z = zeta(s)
l = [0]*n
for i in z:
	l[i]+=1
cum = [l[-1]]
for i in range(n-2,-1,-1):
	cum.append(l[i]+cum[-1])
cum = cum[::-1]
ans = [(n,1)]
for i in range(n-1,0,-1):
	if(i+z[i]==n):
		ans.append((n-i,cum[n-i]+1))

print(len(ans))
for i in sorted(ans):
	print(*i)


