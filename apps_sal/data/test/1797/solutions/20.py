
bz=[0 for i in range(1000000)]
to=[0 for i in range(1000000)]
n=0
n=int(input())
i=1
for x in (input().split()):
	to[i]=int(x)
	i+=1
all_num=0
mx1=0
mx2=0
for i in range(1,n+1):
	if (bz[i]==0):
		x=i
		num=0;
		while (bz[x]==0):
			num+=1
			bz[x]=1
			x=to[x]
		all_num+=num**2
		if (mx1<=num):
			mx1,mx2=num,mx1
		elif mx2<num:
			mx2=num

print(all_num-(mx1**2)-(mx2**2)+((mx1+mx2)**2))
			

