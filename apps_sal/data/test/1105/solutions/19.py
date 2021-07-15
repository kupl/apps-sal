def adds(s,x,k):
	if k in s.keys():
		xs=s[k]
		if x<=xs:
			return 0
		else:
			if x-1==xs:
				s[k]=x
				return 0
			else:
				return 1
	else:
		if x==0:
			s[k]=0
			return 0
		else:
			return 1

def corr(v):
	s=dict()
	for c in v:
		if adds(s,c[0],c[1]):
			return 0
	return 1

n=int(input())
v=[]
for c in range(n):
	x,k=map(int,input().split(' '))
	v.append((x,k))
if corr(v):
	print('YES')
else:
	print('NO')
