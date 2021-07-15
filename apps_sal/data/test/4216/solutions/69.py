N=int(input())

def divisor(n):
	i=1
	table=[]
	while i*i<=n:
		if n%i==0:
			table.append(n//i)
		i+=1
	num=min(table)
	ans=len(str(num))
	return ans
  
print(divisor(N))
