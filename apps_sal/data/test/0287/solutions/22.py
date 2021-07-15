n,k=[int(i)for i in input().split()]
if k==n:
	print(0,0)
	return
if k==0:
	print(0,0)
	return		
a = 1
b=0
h = n//3
if k<=h:
	b = 2*k
else :
	k-=h
	b = h*2 + n%3
	if n%3>0:
	  	k-=1
	  	b-=1  	
	b -=k
print(a,b)	  	




