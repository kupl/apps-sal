import bisect

n,m = map(int,input().split())
C=sorted(list(set(map(int,input().split()))))
T=sorted(list(set(map(int,input().split()))))

r=0
for x in C:
	ind=bisect.bisect_left(T,x)
	if(ind==len(T) or T[ind] != x):
		if ind==0:
			r=max(r,T[ind]-x)
		elif ind==len(T):
			r=max(r,x-T[ind-1])
		else:
			r=max(r,min(T[ind]-x,x-T[ind-1]))
print(r)
