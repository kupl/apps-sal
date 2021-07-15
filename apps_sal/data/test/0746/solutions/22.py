import math
a,b=list(map(int,input().split()))
n=int(input())

x,y,v=list(map(int,input().split()))
mn=math.sqrt((x-a)*(x-a)+(y-b)*(y-b))/v

for i in range(n-1):
	x,y,v=list(map(int,input().split()))
	t=math.sqrt((x-a)*(x-a)+(y-b)*(y-b))/v
	if(t<mn):
		mn=t
print(mn)

