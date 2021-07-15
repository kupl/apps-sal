(n,k,a,b)=list(map(int,input().split()))
l=list(map(int,input().split()))
l.sort()
def se(st,en):
	nonlocal l
	c=0
	lo=0
	hi=len(l)-1
	while lo<=hi:
		mid=(lo+hi)//2
		if l[mid]<=en:
			lo=mid+1

		else:
			hi=mid-1

	c+=hi
	lo=0
	hi=len(l)-1
	while lo<=hi:
		mid=(lo+hi)//2
		if l[mid]>=st:
			hi=mid-1

		else:
			lo=mid+1

	return c-lo+1





def f(st,en):
	#print(st,en)
	"""
	if c>20:
		return 0

	else:
		c+=1"""
	
	nonlocal n,a,b
	t=se(st,en)
	#print(st,en,t)
	if st==en:
		if t==0:
			#print("A:",a,st,en)
			return a

		else:
			#print("B:",b*t*1,st,en)
			return b*t*1

	else:
		le=(en-st+1)
		if t==0:
			#print("A:",a,st,en)
			return a

		else:
			return min(b*t*le,f(st,st+le//2-1)+f(st+le//2,en))
			#print("J",j,st,en)
			#return j


print(f(1,2**n))
#print(se(l,3,4))

