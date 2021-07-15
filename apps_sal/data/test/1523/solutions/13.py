n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
no_id=[1]*k
pers_kn=[]
for i in range(k):
	pers_kn.append([])
for i in range(n):
	pers_kn[a[i]-1].append(i)
	no_id[a[i]-1]=0
no_job=sum(no_id)
cans=[]
for p in pers_kn:
	if len(p)>1:
		mx_index=0
		mx=0
		for t in p:
			if b[t]>mx:
				mx=b[t]
				mx_index=t
		for t in p:
			if t!=mx_index:
				cans.append(b[t])
cans.sort()
print(sum(cans[:no_job]))

