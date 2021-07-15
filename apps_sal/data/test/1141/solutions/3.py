n,m = list(map(int,input().split()))
s = input()
li = list(s)
for i in range(m):
	l,r,c1,c2 = input().split()
	for i in range(int(l)-1,int(r)):
		if li[i]==c1:
			li[i]=c2
print("".join(li))

