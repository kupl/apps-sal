s,v1,v2,t1,t2=[int(x) for x in input().split()]
if t1*2+s*v1<t2*2+s*v2:
	print("First")
if t1*2+s*v1==t2*2+s*v2:
	print("Friendship")
if t1*2+s*v1>t2*2+s*v2:
	print("Second")

