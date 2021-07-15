n=int(input())
v=0
for i in range(n):
	a,b,x,y=map(int,input().split())
	v+=(x-a+1)*(y-b+1)
print(v)
