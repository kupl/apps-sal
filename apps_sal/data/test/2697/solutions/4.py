from math import ceil
def is_prime(x):
	if x==2:
		return True
	for i in range(2,ceil(x**0.5)+1):
		if x%i==0:
			return False
	return True
count = 0
n = int(input())
for i in range(2,n+1):
    if is_prime(i):
        count+=1
print(count)        
