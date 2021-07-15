from collections import defaultdict
x, y = map(int, input().split())
if y%x != 0: 
	print(0)
	return
x = y//x
divisors = []
for i in range(1,int(x**(.5))+1):
	if x%i == 0:
		divisors.append(i)
		divisors.append(x//i)
if divisors[-1] == divisors[-2]: divisors.pop()
divisors.sort()
va = defaultdict(int)
va[1] = 1
mod = 10**9 + 7
for i in range(1, len(divisors)):
	k = divisors[i]
	count = pow(2,k-1,mod)
	for j in range(i):
		if k%divisors[j] == 0: count = (count-va[divisors[j]])%mod
	va[k] = count
print(va[x])
