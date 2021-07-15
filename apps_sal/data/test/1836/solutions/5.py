import sys

l=0
ady = [[]]
ady2 = [[]]
for line in sys.stdin:
	if l==0:
		n,m = line.split()
		n = int(n)
		m = int(m)
		ady = [[] for i in range(n)]
		ady2 = [[] for i in range(n)]
	else:
		a,b = list(map(int,line.split())) 
		a = int(a)-1
		b = int(b)-1
		ady2[a].append(b)
		ady2[b].append(a)
		if a>b: ady[a].append(b)
		else: ady[b].append(a)
	l+=1

c=[0]*n

def colamaslarga(a):
	if (len(ady[a])==0):
		c[a]=1
		return 1
	elif c[a]!=0:
		return c[a]
	else:
		res=max([colamaslarga(ad) for ad in ady[a]])+1
		c[a]=res
		return res

mx = 0
for i in range(n):
	cl = colamaslarga(i)
	res = cl*len(ady2[i])
	if res>mx: mx=res

print (mx)

