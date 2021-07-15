i1=input().split();
x=int(i1[0])
y=int(i1[1])
if (y%2==1 and x%2==1 ) or (y%2==0 and x%2==0) or (y<=1 and x>0) or (y>x+1):
	print ("No")
else:
	print ("Yes")

