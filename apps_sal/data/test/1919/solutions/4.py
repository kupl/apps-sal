import sys
def fact(n):
	ret = 1
	for x in range(1, n + 1):
		ret = ret * x
	return ret

def C(n, k):
	return fact(n) // (fact(k) * (fact(n - k)))
n = int(input())
if n % 2 == 1:
	print(1)
else:
	print(2)
