
n=int( input() )
s=str( input() )

ret=3
for i in range(1,n):
	if s[i] != s[i-1]:
		ret=ret+1

if ret < n :
	print (ret)
else :
	print (n) 

