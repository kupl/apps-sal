n = int(input())
s = ''
if (n % 2) == 0:
	for i in range(n // 2):
		s += '1'
else:
	s += '7'
	for i in range((n - 3) // 2):
		s += '1'
print(s)

