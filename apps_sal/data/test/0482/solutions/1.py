n, k = input().split()
n, k = int(n), int(k)
s = []
for i in range(n):
	s.append(chr((i % k + ord('a'))))
print(''.join(s))
