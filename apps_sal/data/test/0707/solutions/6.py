n, m = list(map(int,input().split()))
x = list(map(int,input().split()))
p = list(map(int,input().split()))
def gcd(a, b):
	if a == 0:
		return b
	if b == 0:
		return a
	if a > b:
		a, b = b, a
	return gcd(a, b % a)
gie = x[1] - x[0]
for i in range(2,n):
	gie = gcd(gie, x[i]-x[i-1])
import sys
for i in range(m):
	if gie % p[i] == 0:
		print("YES")
		print(x[0], end =  " ")
		print(i + 1)
		return
print("NO")
#print(gcd(7,14))
