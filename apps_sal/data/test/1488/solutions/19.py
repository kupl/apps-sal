import math
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
k = 0
s1 = 0
s2 = 0
for i in a:
	s2 += s1 - k * i
	s1 += i
	k += 1
s2 *= 2
s2 += sum(a)
gcd = math.gcd(s2, n)
print(s2 // gcd, n // gcd)


