n = int(input())

def naive(n):
	c=0
	#print(n,end='\t')
	while n!=0:
		c+=1
		n-=max([int(x) for x in list(str(n))])
		#print(n)
	print(c)

# d=dict()
# d[0]=0
# def dp(n):
# 	if(n==0):
# 		return 0
# 	s=[int(x) for x in list(str(n))]
# 	minimo=n
# 	s=max(s)
# 	temp = n - s
# 	return dp(temp)+1

# for x in range(1,10,1):
# 	naive(x)
# for x in range(10,100,10):
# 	naive(x)
# for x in range(100,1000,100):
# 	naive(x)
# for x in range(1000,10000,1000):
# 	naive(x)
# for x in range(5000,6000,100):
# 	naive(x)

naive(n)
