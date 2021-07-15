n=int(input())
l=list(map(lambda x:int(x)*2,input().split(" ")))
t=list(map(lambda x:"GWL".index(x),input()))
mins=[0 for i in range(0,n+1)]
for i in range(n-1,-1,-1):
	if t[i]!=2:mins[i]=max(mins[i+1]-l[i],0)
	else:mins[i]=mins[i+1]+l[i]
curs=ans=st=0
for i in range(0,n):
	if(t[i]==0):
		curs+=l[i];ans+=l[i]*5
		if(curs>mins[i+1]):
			ol=(curs-mins[i+1])//2
			ol=min(ol,l[i])
			ans-=4*ol;curs-=2*ol
	if(t[i]==1):
		st=1;curs+=l[i];ans+=l[i]*3
	if(t[i]==2):
		if(curs<l[i]):
			ol=l[i]-curs;curs=l[i]
			ans+=ol*(3 if st else 5)
		curs-=l[i];ans+=l[i]
if curs>0:ans-=curs//2*2
print(ans//2)
