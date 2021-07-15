n,k,c=map(int,input().split())
s=input()
l=list();r=list()
nex=0
for i in range(n):
	if i<nex:
		continue
	if s[i]=="o":
		nex=i+c+1
		l.append(i)
		if len(l)==k:
			break
nex=-1
for i in range(n):
	if i<nex:
		continue
	if s[-i-1]=="o":
		nex=i+c+1
		r.append(n-i-1)
		if len(r)==k:
			break
r=r[::-1]
for i in range(k):
	if l[i]==r[i]:
		print(l[i]+1)
