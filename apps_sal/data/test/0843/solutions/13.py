n = int(input())
s = input(); a = len(s)
j = list(map(int, input().split()))
x = 1
b = 'INFINITE'
tmp = 0
while tmp < n:
	if s[x-1] == '>':
		x += j[x-1]
		if x > n:
			b = 'FINITE'; break
	elif s[x-1] == '<':
		x -= j[x-1]
		if x <= 0:
			b = 'FINITE'; break
	tmp += 1
print(b)
