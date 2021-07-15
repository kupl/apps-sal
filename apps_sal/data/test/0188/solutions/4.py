def func(a):
	if(a<0):
		return 0
	else:
		return a

n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
two = 2*n
four = n
baki=[]
for val in l:
	if(val>=4):
		ans=min(four,val//4)
		val=val-ans*4
		four-=ans
	ans=min(two,(val)//2)
	val=val-ans*2
	two-=ans
	baki.append(func(val))
store=sum(baki)
if(store==0):
	print("YES")
elif(store>0 and four==0 and two==0):
	print("NO")
else:
	baki.sort(reverse=True)
	cap1=four
	cap2=four
	for val in baki:
		if(val==3):
			if(cap1>0 and cap2>0):
				cap1-=1
				cap2-=1
			else:
				two-=2
		elif(val==2):
			if(two>0):
				two-=1
			else:
				if(cap1>0):
					cap1-=1
				else:
					cap2-=2
		elif(val==1):
			if(cap2>0):
				cap2-=1
			elif(cap1>0):
				cap1-=1
			else:
				two-=1
	if(cap2<0 or cap1<0 or two<0):
		print("NO")
	else:
		print("YES")
		



		



