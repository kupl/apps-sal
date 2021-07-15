import sys
input = sys.stdin.readline
I = lambda : list(map(int,input().split()))

n,=I()
l=I()
an=[]
sv=[0]*(10**5+10)
for i in range(2,len(sv)):
	if not sv[i]:
		sv[i]=i
		for j in range(2*i,len(sv),i):
			sv[j]=1
sv[0]=sv[1]=1
for i in range(2,len(sv)):
	if not sv[i]-1:
		sv[i]=sv[i-1]
ix=[0]*(n+1)
for i in range(n):
	ix[l[i]]=i
for i in range(n):
	ct=0
	while l[i]!=i+1 and ct<5:
		cr=ix[i+1]
		pr=sv[cr-i+1]
		#print(i,cr,pr)
		an.append(sorted([cr+1,cr-pr+2]))
		l[cr],l[cr-pr+1]=l[cr-pr+1],l[cr]
		ix[l[cr]],ix[l[cr-pr+1]]=ix[l[cr-pr+1]],ix[l[cr]]
		ct+=1
print(len(an))
for i in an:
	print(*i)
