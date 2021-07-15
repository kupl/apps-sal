s,v1,v2,t1,t2=map(int,input().split())
a,b=t1*2+s*v1,t2*2+s*v2
if a<b:
	print("First")
elif a>b:
	print("Second")
else:
	print("Friendship")
