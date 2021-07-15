


str=input().split()
n,a,b=[int(str[x]) for x in range(0,3)]
inv=0
if (b!=1):
	t=a
	a=b
	b=t
	inv=1
	
if (b!=1 or n>1 and n<4 and a==1 and b==1):
	print ('NO')
	return

print ('YES')
	
f=[[0]*n for i in range(0,n)]
#print (f)

for i in range(0,n-a):
	f[i][i+1]=f[i+1][i]=1
#f[0][1]=1

#print (f[0][1],f[1][1],f[2][1])

for i in range(0,n):
	cur=[chr(((f[i][j]^inv)&(i!=j))+48) for j in range(0,n)]
	print (''.join(cur))
