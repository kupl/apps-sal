n, m = map(int, input().split())

total = 0

if m%n!=0:
	print(-1)
	return

v = m//n

while v%2==0:
	total += 1
	v //= 2
while v%3==0:
	total += 1
	v //= 3
if v!=1:
	print(-1)
	return
print(total)
