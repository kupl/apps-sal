n,p=[int(x) for x in input().split()]
mi=[]
for k in range(0,n):
	l,r=[int(x) for x in input().split()]
	#Probability that prime number multiple chosen in  list.
	x=(r//p- (l-1)//p)/(r-l+1)
	#1-x is Probability that it is not prime number multiple.
	mi.append(1-x)

#print(mi)
fin=0
for z in range(0,len(mi)):
	fin+=(1-mi[z]*mi[(z+1)%n])
print(fin*2000)

