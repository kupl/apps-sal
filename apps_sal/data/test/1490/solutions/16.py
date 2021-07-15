n,m=map(int,input().split())
inp=list(map(int,input().split()))
inp=set(inp)
count=1
st=[0]*100000
a=0
while((m-count)>=0):
	if(not(count in inp)):
		st[a]=count
		a+=1
		m-=count
		inp.add(count)
	count+=1
print(a)
for i in range(a):
	print(st[i], end=" ")
