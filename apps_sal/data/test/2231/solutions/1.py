import sys
f=sys.stdin
out=sys.stdout

def fun(l,b):
	return (((2*(l+b))**2)/(l*b))

t=int(f.readline().rstrip('\r\n'))
for _ in  range(t):
	n=int(f.readline().rstrip('\r\n'))
	a=list(map(int,f.readline().rstrip('\r\n').split()))
	d={}
	arr=[]
	for i in a:
		if i in d:
			d[i]+=1
		else:
			d[i]=1
			arr.append(i)
	arr.sort()
	mi=float('inf')
	tmp=-1
	l1,b1=-1,-1
	for i in range(len(arr)):
		if tmp==-1:
			if d[arr[i]]>=4:
				tmp=arr[i]
				pmi=mi
				mi=min(mi,fun(arr[i],arr[i]))
				if pmi!=mi:
					l1,b1=arr[i],arr[i]
			elif d[arr[i]]>=2:
				tmp=arr[i]
		else:
			if d[arr[i]]>=4:
				tmp=arr[i]
				pmi=mi
				mi=min(mi,fun(arr[i],arr[i]))
				if pmi!=mi:
					l1,b1=arr[i],arr[i]
			elif d[arr[i]]>=2:
				pmi=mi
				mi=min(mi,fun(tmp,arr[i]))
				if pmi!=mi:
					l1,b1=tmp,arr[i]
				tmp=arr[i]
	out.write(str(l1)+" "+str(l1)+" "+str(b1)+" "+str(b1)+"\n")
