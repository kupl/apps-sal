#input

n,m=list(map(int,input().split()))
d_1=[]
d_2=[]
for i in range(m):
	x,y=list(map(str,input().split()))
	d_1.append(x)
	d_2.append(y)

l=[str(x) for x in input().split()]


#variables



#main

for i in range(n):
	if len(d_2[d_1.index(l[i])])<len(l[i]):
		l[i]=d_2[d_1.index(l[i])]



#output
print(''.join([str(l[i])+' ' for i in range(n)]))

