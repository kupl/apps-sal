import math
n, k = list(map(int, input().split()))
a = 1;
ar = list(map(int, input().split()))
for c in ar:
	a *=  math.gcd(k,c) //math.gcd(a, c)
if a % k == 0:
	print("Yes")
else:
	print("No")


