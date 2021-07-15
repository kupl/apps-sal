a,b=map(int,input().split())
o=0
while(a and b):
	o=o+max(a,b)//min(a,b)
	if(a>b):a=a%b
	else:b=b%a
print(o)
