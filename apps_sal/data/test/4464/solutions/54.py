from fractions import gcd
A, B, C = map(int, input().split())
if C % gcd(A, B) == 0:
	print("YES")
else:
	print("NO")
