import math 
def div(n):
	cnt = 0
	for i in range(1, (int)(math.sqrt(n)) + 1):
		if (n % i == 0): 
			if (n / i == i) : 
				cnt+=1
			else: 
				cnt+=2
	return cnt
b=int(input())
if b==1:
	print (1)
else:
	print (div(b))
