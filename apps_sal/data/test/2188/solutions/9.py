def func(i):
	return 0-ar[i][0]
def func2(i):
	return ar[i][0]
n=int(input())
ar=[[0 for x in range(2)] for y in range(n)]
for i in range(n):
	ar[i][0],ar[i][1]=map(int,input().split())
mn=[]
mx=[]
for i in range(n):
	if(ar[i][0]<ar[i][1]):
		mn.append(i)
	else:
		mx.append(i)
if(len(mn)>len(mx)):
	mn=sorted(mn, key = func)
	print(len(mn))
	for x in mn:
		print (x+1,end=" ")
else:
	# mx=sorted(mx,reverse=True)
	mx=sorted(mx, key = func2)
	print(len(mx))
	for x in mx:
		print (x+1,end=" ")

