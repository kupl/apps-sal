def gcd(a, b):
	if (b == 0):
		return a
	return gcd(b, a % b)


n = int(input())
a = sorted(list(map(int, input().split())),reverse = True)
k = 0
s1 = 0
s2 = 0
for i in a:
	s2 += s1 - k * i
	s1 += i
	k += 1
s2 *= 2
s2 += sum(a)
gc = gcd(s2, n)
print(s2 // gc, n // gc)


