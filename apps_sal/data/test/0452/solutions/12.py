
def gcd(a, b):
	if (b == 0):
		return a
	else:
		return gcd(b, a % b)

p, q = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))
g = gcd(p, q)
p = p // g
q = q // g
k = A[n - 1]
l = 1
for i in range(n - 2, -1, -1):
	k, l = l, k
	k += A[i] * l
	g = gcd(k, l)
	k = k // g
	l = l // g
if (k == p and q == l):
	print ("YES")
else:
	print ("NO")
