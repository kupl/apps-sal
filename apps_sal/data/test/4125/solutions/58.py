import math
from functools import reduce
 
def gcd(*numbers):
	return reduce(math.gcd, numbers)

def gcd_list(numbers):
	return reduce(math.gcd, numbers)

n,X = map(int,input().split())
x = list(map(int,input().split()))
for i in range(n):
	x[i] = x[i] -  X
print(abs(gcd_list(x)))
