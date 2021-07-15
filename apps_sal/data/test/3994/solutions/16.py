n=int(input())
l=list(input())
p=[]
for i in range(n):
	p.append(list(map(int,input().split())))
d=[0]*100001
for i in range(n):
	a,b=p[i]
	s=int(l[i])
	for j in range(b):
		if s:
			d[j]+=1
	for j in range(b,100001):
		if (j-b)%a==0:
			s=1-s
		if s:
			d[j]+=1

print(max(d))

