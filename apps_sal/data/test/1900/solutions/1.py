#reference sol:-31772413
r=lambda:list(map(int,input().split()))
n,k,m=r()
a=list(r())
stck=[]
for i in range(n):
	if len(stck)==0 or stck[-1][0]!=a[i]:
		stck.append([a[i],1])
	else:
		stck[-1][1]+=1
	if stck[-1][1]==k:
		stck.pop()

rem=0
strt,end=0,len(stck)-1
if m > 1:
	while end-strt+1 > 1 and stck[strt][0]==stck[end][0]:
		join=stck[strt][1]+stck[end][1]
		if join < k:
			break
		elif join % k==0:
			rem+=join
			strt+=1
			end-=1

		else:
			stck[strt][1]=join % k
			stck[end][1]=0
			rem+=(join//k)*k

tr=0
slen=end-strt+1
for el in stck[:slen]:
	tr+=el[1]
if slen==0:
	print(0)
elif slen==1:
	r=(stck[strt][1]*m)%k
	if r==0:
		print(0)
	else:
		print(r+rem)
else:
	print(tr*m+rem)

