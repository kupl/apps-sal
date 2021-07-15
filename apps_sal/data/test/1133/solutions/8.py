n=int(input())
i=0
x=[]
while i<n:
	x.append(str(input()))
	i+=1
i=25
r=0
while i:
	j=i
	while j:
		j-=1
		t=0
		k=n
		while k:
			k-=1
			y=x[k]
			z=len(y)
			ok=1
			while z:
				z-=1
				if ord(y[z])-ord('a')!=i:
					if ord(y[z])-ord('a')!=j:ok=0
			if ok:t+=len(y)
		if r<t:r=t
	i-=1
print(r)

