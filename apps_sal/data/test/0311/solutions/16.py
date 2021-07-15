x,y,z,t1,t2,t3=list(map(int,input().strip().split()))
T1=abs(y-x)*t2+abs(z-x)*t2+t3*3
T2=abs(y-x)*t1
if (T1<=T2):
	print ("YES")
else:
	print ("NO")
