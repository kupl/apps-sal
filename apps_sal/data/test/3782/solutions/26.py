n,k,q=map(int,input().split())
a=list(map(int,input().split()))
ans=10**10
for y in a:
	t=[[]]
	for i in a:
		if i<y:
			if len(t[-1]):t.append([])
		else:
			t[-1].append(i)
	if len(t[-1])==0:del t[-1]
	m=[]
	for i in t:
		if len(i)<k:continue
		m+=sorted(i)[:len(i)-k+1]
	if len(m)<q:continue
	m.sort()
	ans=min(ans,m[q-1]-y)
print(ans)
