a=input().split()
n=int(a[0])
m=int(a[1])

kn=[]
k=input().split()
for i in range(n):
	kn+=[int(k[i])]

c=0
for i in range(m):
	c+=kn.count(i+1)*(n-kn.count(i+1))
print(int(c/2))
