#55 ABC135E
k=int(input())
x,y=map(int,input().split())
def golf(a,b):
	if a<0:
		t=golf(-a,b)
		return -t[0],t[1]
	if b<0:
		t=golf(a,-b)
		return t[0],-t[1]
	if a>b:
		t=golf(b,a)
		return t[1],t[0]
	if a+b>=2*k:
		return a,b-k
	if a+b==k:
		return 0,0
	r=k-(a+b)//2
	return -r,a+b+r-k
if k%2==0 and (x+y)%2==1:
	print(-1)
else:
	res=[]
	while x or y:
		res.append([x,y])
		x,y=golf(x,y)
	print(len(res))
	for r in res[::-1]:
		print(r[0],r[1])
