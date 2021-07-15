n = int(input())
lc = None
for c in input():
	if (lc is None) or (lc == c):
		lc = c
	else:
		n -= 1
		lc = None
print(n)

