n=int(input())
L=list(map(int,input().split()))
L.sort(reverse=True)


import collections
d=collections.Counter(L)
M=0
m=[0,0]
for v in d:
	if d[v]>=4:
		M=max(M,v)
	elif d[v]>=2:
		m.append(v)
m.sort(reverse=True)

print(max(M**2,m[0]*m[1],M*m[0]))
